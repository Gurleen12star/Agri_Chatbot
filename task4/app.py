from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from database import db, init_db, User, ChatHistory
from chatbot_model import translate_text, detect_language
import openai, os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = "secret123"
init_db(app)

# Configure upload folder
UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Admin credentials
ADMIN_USER = "admin"
ADMIN_PASS = "admin123"

# OpenAI API Key (set your own key here or as environment variable)
openai.api_key = os.getenv("OPENAI_API_KEY", "sk-your-key-here")

# ---------- Existing Routes (same as Task 3) ----------
@app.route("/")
def index():
    if "user_id" in session:
        return redirect(url_for("chat"))
    return render_template("index.html")

@app.route("/", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    user = User.get_by_username(username)
    if user and user.check_password(password):
        session["user_id"] = user.id
        session["username"] = user.username
        flash("Login successful!", "success")
        return redirect(url_for("chat"))
    flash("Invalid username or password", "error")
    return redirect(url_for("index"))

@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if User.get_by_username(username):
            flash("Username already exists", "error")
        else:
            User.create(username, password)
            flash("Account created successfully!", "success")
            return redirect(url_for("index"))
    return render_template("register.html")

@app.route("/chat")
def chat():
    if "user_id" not in session:
        return redirect(url_for("index"))
    user_id = session["user_id"]
    chats = ChatHistory.query.filter_by(user_id=user_id).all()
    return render_template("chat.html", username=session["username"], chats=chats)

@app.route("/chat", methods=["POST"])
def chat_post():
    if "user_id" not in session:
        return jsonify({"response": "Please login first."})
    msg = request.form["message"]
    lang = request.form["lang"]
    detected = detect_language(msg)
    translated = translate_text(msg, dest="en")
    response = f"You said: {translated}. (Detected: {detected})"
    ChatHistory.create(session["user_id"], msg, response)
    if lang != "en":
        response = translate_text(response, dest=lang)
    return jsonify({"response": response})

@app.route("/logout")
def logout():
    session.clear()
    flash("Logged out successfully.", "success")
    return redirect(url_for("index"))

@app.route("/admin", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username == ADMIN_USER and password == ADMIN_PASS:
            session["admin"] = True
            return redirect(url_for("admin_dashboard"))
        flash("Invalid credentials", "error")
    return render_template("admin_login.html")

@app.route("/admin/dashboard")
def admin_dashboard():
    if not session.get("admin"):
        return redirect(url_for("admin_login"))
    users = User.query.all()
    chats = ChatHistory.query.all()
    return render_template("admin_dashboard.html", users=users, chats=chats)

# ---------- NEW: Image Analysis ----------
@app.route("/image_analysis", methods=["GET","POST"])
def image_analysis():
    if "user_id" not in session:
        return redirect(url_for("index"))

    result = None
    img_path = None

    if request.method == "POST":
        file = request.files.get("image")
        if file:
            filename = secure_filename(file.filename)
            path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(path)
            img_path = path

            # Analyze image with OpenAI Vision
            try:
                response = openai.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": "You are an agriculture assistant that analyzes plant and crop images."},
                        {"role": "user", "content": [
                            {"type": "text", "text": "Describe this image and identify any visible crop diseases."},
                            {"type": "image_url", "image_url": f"http://localhost:5000/{path}"}
                        ]}
                    ]
                )
                result = response.choices[0].message.content
            except Exception as e:
                result = f"⚠️ Error analyzing image: {e}"

    return render_template("image_analysis.html", result=result, img_path=img_path)

if __name__ == "__main__":
    app.run(debug=True)

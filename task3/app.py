from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from database import db, init_db, User, ChatHistory
from chatbot_model import translate_text, detect_language
import os

app = Flask(__name__)
app.secret_key = "secret123"
init_db(app)

ADMIN_USER = "admin"
ADMIN_PASS = "admin123"

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
    else:
        flash("Invalid username or password", "error")
        return redirect(url_for("index"))

@app.route("/register", methods=["GET", "POST"])
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

if __name__ == "__main__":
    app.run(debug=True)

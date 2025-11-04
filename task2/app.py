from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from chatbot_model import get_bot_response
from database import db, User, Admin
import os

app = Flask(__name__)
app.secret_key = "secretkey123"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chatbot.db'

db.init_app(app)
bcrypt = Bcrypt(app)

# ---------- ROUTES ----------

@app.route('/')
def home():
    if 'user_id' in session:
        return redirect(url_for('chat'))
    return redirect(url_for('login'))


# ---------- USER REGISTRATION ----------
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = bcrypt.generate_password_hash(request.form['password']).decode('utf-8')

        if User.query.filter_by(username=username).first():
            flash('Username already exists!', 'error')
            return redirect(url_for('register'))

        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')


# ---------- USER LOGIN ----------
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()

        if user and bcrypt.check_password_hash(user.password, password):
            session['user_id'] = user.id
            session['username'] = user.username
            flash('Login successful!', 'success')
            return redirect(url_for('chat'))
        else:
            flash('Invalid username or password', 'error')
    return render_template('index.html')


# ---------- ADMIN LOGIN ----------
@app.route('/admin', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        admin = Admin.query.filter_by(username=username).first()

        if admin and bcrypt.check_password_hash(admin.password, password):
            session['admin_id'] = admin.id
            flash('Admin login successful!', 'success')
            return redirect(url_for('admin_dashboard'))
        else:
            flash('Invalid admin credentials', 'error')
    return render_template('admin_login.html')


# ---------- ADMIN DASHBOARD ----------
@app.route('/admin/dashboard')
def admin_dashboard():
    if 'admin_id' not in session:
        return redirect(url_for('admin_login'))
    users = User.query.all()
    return render_template('admin_dashboard.html', users=users)


# ---------- CHAT ----------
@app.route('/chat')
def chat():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('chat.html', username=session['username'])


# ---------- CHATBOT API ----------
@app.route('/get', methods=['POST'])
def get_bot():
    data = request.get_json()
    user_msg = data['message']
    bot_reply = get_bot_response(user_msg)
    return jsonify({'response': bot_reply})


# ---------- LOGOUT ----------
@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))


# ---------- RUN ----------
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

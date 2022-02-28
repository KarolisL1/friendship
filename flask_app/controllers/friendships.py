from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User
from flask_app.models.friendship import Friendship

@app.route('/')
def index():
    return redirect('/dashboard')

@app.route("/dashboard")
def dashboard():
    users = User.all_users()
    friendship = User.all_friendships()
    return render_template('dashboard.html', users=users, friendship=friendship)

@app.route("/add_user", methods=['POST'])
def add_user():
    User.user_registration(request.form)
    return redirect('/dashboard')

@app.route("/create_friendship", methods=['POST'])
def create_friendship():
    # print(request.form['user_id'])
    # print(request.form['friend_id'])
    # data = {
    #     'user_id': request.form['user_id'],
    #     'friend_id': request.form['friend_id']
    # }
    Friendship.friendship_registration(request.form)
    return redirect('/dashboard')
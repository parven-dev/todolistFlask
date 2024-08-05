from flask import render_template, request
from flask_app.form import UserLogin, SignUp
from database import User

from main import app, db


@app.route("/")
def hello_world():
    return "<h1>Welcome</h1>"


@app.route('/login')
def login():
    user_login = UserLogin()
    return render_template("/login.html", login=user_login)


@app.route("/todo", methods=["GET", "POST"])
def todoList():
    if request.method == "POST":
        topic = request.form["text"]
        options = request.form["options"]
        print(options)
    return render_template("/index.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    user_signup = SignUp()
    if request.method == "POST" or user_signup.validate():
        name = user_signup.name.data
        email = user_signup.email.data
        password = user_signup.password.data
        confirm_password = user_signup.confirm_password.data

        if password == confirm_password:
            add_users = User(db_name=name,
                             db_email=email,
                             db_password=password,
                             db_confirm_password=password
                             )
            db.session.add(add_users)
            db.session.commit()

        return f"name: {name}, email: {email}, password: {password}, confirm_password: {confirm_password}"
    else:
        print("not in")
        return render_template("/signup.html", signup=user_signup)

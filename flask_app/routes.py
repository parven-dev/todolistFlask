from flask import render_template, request
from flask_app.form import UserLogin, SignUp

from main import app


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route('/login')
def login():
    user_login = UserLogin()
    return render_template("/login.html", login=user_login)


@app.route("/signup", methods=["GET", "POST"])
def signup():
    user_signup = SignUp()
    if request.method == "POST" or user_signup.validate():
        name = user_signup.name.data
        email = user_signup.email.data
        password = user_signup.password.data
        confirm_password = user_signup.confirm_password.data

        return f"name: {name}, email: {email}, password: {password}, confirm_password: {confirm_password}"
    else:
        print("not in")
        return render_template("/signup.html", signup=user_signup)

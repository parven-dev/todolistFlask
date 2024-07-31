from flask import render_template
from flask_app.form import UserLogin

from main import app


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route('/login')
def login():
    user_login = UserLogin()
    return render_template("/login.html", login=user_login)

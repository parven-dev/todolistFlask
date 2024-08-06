from flask import render_template, request, session, redirect

from flask_app.form import UserLogin, SignUp
from database import User, TodoList

from main import app, db

from flask_login import (
    UserMixin,
    login_user,
    LoginManager,
    current_user,
    logout_user,
    login_required,
)

login_manager = LoginManager()
login_manager.init_app(app)

login_manager.session_protection = "strong"
login_manager.login_view = "login"
login_manager.login_message_category = "info"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/login', methods=["GET", "POST"])
def login():
    print('fuk')
    user_login = UserLogin()
    if user_login.validate() or request.method == "POST":
        print("you")
        user = User.query.filter_by(db_email=user_login.email.data).first()
        print(user)
        if user and user.db_password == user_login.password.data:
            print(user)
            login_user(user)
            print("yes i m login")
            return "<h2> you login successfully </h2>"
        else:
            print('i m not')
            return "<h2>email password wrong</h2>"
    return render_template("/login.html", login=user_login)


@app.route("/", methods=["GET", "POST"])
def todoList():
    show_todo = TodoList.query.all()
    if request.method == "POST":
        topic = request.form["text"]
        options = request.form["options"]

        add_data = TodoList(
            db_task=topic,
            db_priority=options

        )
        db.session.add(add_data)
        db.session.commit()

        return redirect("/")
    return render_template("/index.html", task=show_todo)


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

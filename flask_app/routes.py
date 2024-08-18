from flask import render_template, request, redirect, url_for
from flask_login import login_required, logout_user, login_user, LoginManager, current_user

from flask_app.form import UserLogin, SignUp
from database import User, TodoList

from main import app, db
from names_generator import generate_name


login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.login_view = "login"
login_manager.login_message_category = "info"

login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route("/dashboard")
@login_required
def dashboard():
    user1 = User.query.all()
    todo = TodoList.query.all()

    print(user1, todo)
    return render_template("/dashboard.html", user=user1)


@app.route('/login', methods=["GET", "POST"])
def login():
    user_login = UserLogin()
    if user_login.validate() or request.method == "POST":
        email = user_login.email.data
        password = user_login.password.data
        user = User.query.filter_by(db_email=email).first()

        if user and user.db_password == password:
            login_user(user)
            return redirect(url_for("dashboard"))
        else:
            return redirect(url_for("login"))

    return render_template("/login.html", login=user_login)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))




@app.route("/")
def home():
    return render_template("/home.html")


@app.route("/todo", methods=["GET", "POST"])
def todo():
    todo = TodoList.query.all()
    all_user = User.query.all()
    print(todo)
    if request.method == "POST":
        topic = request.form["text"]
        options = request.form['options']
        add_data = TodoList(
            db_task=topic,
            db_priority=options,
            user_id=current_user.id
        )
        db.session.add(add_data)
        db.session.commit()
        return redirect(url_for("todo"))
    return render_template("/todo.html", todo=todo, users=all_user)


@app.route("/delete/<int:sno>/", methods=["POST", "GET"])
def delete(sno):
    todo_id = TodoList.query.get_or_404(sno)
    db.session.delete(todo_id)
    db.session.commit()
    print("i m inside database")
    return redirect(url_for("login"))


@app.route("/signup", methods=["GET", "POST"])
def signup():
    user_signup = SignUp()
    if user_signup.validate() or request.method == "POST":
        # name = user_signup.username.data
        email = user_signup.email.data
        password = user_signup.password.data
        # confirm_password = user_signup.confirm_password.data

        # if password == confirm_password:
        add_users = User(
            # db_name=name,
            db_email=email,
            db_password=password,
            profile=generate_name()
            # db_confirm_password=password,
                             )
        db.session.add(add_users)
        db.session.commit()

        return redirect(url_for('login'))

    return render_template("/signup.html", signup=user_signup)

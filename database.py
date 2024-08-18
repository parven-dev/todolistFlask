from main import db, app
from flask_login import UserMixin, login_user


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    # db_name = db.Column(db.String, unique=True, nullable=False)
    db_email = db.Column(db.String)
    db_password = db.Column(db.String)
    profile = db.Column(db.String)
    # db_confirm_password = db.Column(db.String)
    # todo_list = db.relationship("TodoList", backref="user", lazy="dynamic")
    todolist = db.relationship("TodoList", backref="user", lazy=True)

    def __repr__(self):
        return f" '{self.db_email}')"


class TodoList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    db_task = db.Column(db.String)
    db_priority = db.Column(db.String)
    # todo_id = db.Column(db.Integer, db.ForeignKey("todo.id"), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)


with app.app_context():
    db.create_all()

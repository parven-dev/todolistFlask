from main import db, app
from flask_login import UserMixin, login_user

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    db_name = db.Column(db.String, unique=True, nullable=False)
    db_email = db.Column(db.String)
    db_password = db.Column(db.String)
    db_confirm_password = db.Column(db.String)
    todo_list = db.relationship("TodoList", backref="user", lazy="dynamic")

    def __repr__(self):
        return f"User('{self.db_name}', '{self.db_email}')"

class TodoList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    db_task = db.Column(db.String)
    db_priority = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

with app.app_context():
    db.create_all()


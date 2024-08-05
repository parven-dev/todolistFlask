from main import db, app


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    db_name = db.Column(db.String, unique=True, nullable=False)
    db_email = db.Column(db.String)
    db_password = db.Column(db.String)
    db_confirm_password = db.Column(db.String)


class TodoList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    db_task = db.Column(db.String)
    db_priority = db.Column(db.String)


with app.app_context():
    db.create_all()

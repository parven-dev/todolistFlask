from flask_wtf import FlaskForm

from wtforms import (StringField, TextAreaField, IntegerField, SubmitField)
from wtforms.validators import input_required, length, Email, DataRequired


class UserLogin(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = StringField("Password", validators=[DataRequired()])

    submit = SubmitField("submit")

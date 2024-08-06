from flask_wtf import FlaskForm
import email_validator


from wtforms import (StringField, TextAreaField, IntegerField, SubmitField)
from wtforms.validators import input_required, length, Email, DataRequired



class UserLogin(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = StringField("Name", validators=[DataRequired()])
    submit = SubmitField("submit")


class SignUp(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = StringField("Password", validators=[DataRequired()])
    confirm_password = StringField("Confirm Password", validators=[DataRequired()])
    submit = SubmitField("submit")


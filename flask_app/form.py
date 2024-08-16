from flask_wtf import FlaskForm
import email_validator

from wtforms import (StringField, TextAreaField, IntegerField, SubmitField)
from wtforms.fields.simple import PasswordField
from wtforms.validators import input_required, length, Email, DataRequired, InputRequired, Length, Regexp, EqualTo


class UserLogin(FlaskForm):
    email = StringField("Email")
    password = StringField("Name", validators=[DataRequired()])
    submit = SubmitField("submit")


class SignUp(FlaskForm):
    # username = StringField(
    #     validators=[
    #         InputRequired(),
    #         Length(3, 20, message="Please provide a valid name"),
    #         Regexp(
    #             "^[A-Za-z][A-Za-z0-9_.]*$",
    #             0,
    #             "Usernames must have only letters, " "numbers, dots or underscores",
    #         ),
    #     ]
    # )
    email = StringField(
        validators=[DataRequired(), Email(), length(1, 64)])
    password = PasswordField(
        validators=[DataRequired(),
                    length(8, 72)])
    # confirm_password = PasswordField(
    #     validators=[DataRequired(), Length(8, 72),
    #                 EqualTo("password", message="Passwords must match !")])
    submit = SubmitField("submit")

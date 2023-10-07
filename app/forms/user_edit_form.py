from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models.user import User


class EditForm(FlaskForm):
    username = StringField("Insert new username", validators=[DataRequired()])
    email = StringField("Insert new email", validators=[DataRequired(), Email()])
    password = PasswordField("Insert new password", validators=[DataRequired()])
    password2 = PasswordField("Repeat new password", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("Done!")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).count()
        if user >= 1:
            raise ValidationError("Current username is already taken.\nPlease, choose another one.")

    def validate_email(self, email):
        exist_email = User.query.filter_by(email=email.data).count()
        if exist_email >= 1:
            raise ValidationError("Current email is already registered.\nPlease, choose another one.")

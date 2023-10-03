from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models.user import User


class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    password2 = PasswordField("Repeat your password", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("Registrate")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError("Current username is already occupied.\nChoose another one, please.")

    def validate_email(self, email):
        exist_email = User.query.filter_by(email=email.data).first()
        if exist_email is not None:
            raise ValidationError("Current email is already used.\nChoose another one, please.")

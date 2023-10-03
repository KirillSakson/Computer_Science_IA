from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models.user import User


class EditForm(FlaskForm):
    username = StringField("Введите новое/старое имя учётной записи", validators=[DataRequired()])
    email = StringField("Введите новый/старый email", validators=[DataRequired(), Email()])
    password = PasswordField("Введите новый пароль", validators=[DataRequired()])
    password2 = PasswordField("Повторите новый пароль", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("Готово!")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).count()
        if user > 1:
            raise ValidationError("Данное имя пользователя уже занято.\nПожалуйста, выберите другое.")

    def validate_email(self, email):
        exist_email = User.query.filter_by(email=email.data).count()
        if exist_email > 1:
            raise ValidationError("Данный email уже зарегистрирован.\nПожалуйста, выберите другой.")

from wtforms import Form, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, length, Email, EqualTo


class RegisterForm(Form):
    email = StringField('Email', [DataRequired(), length(3, 30, 'Email must be 3-30 characters')])
    password = PasswordField('Password', [DataRequired(), length(6, 20, 'Password must be 6-20 characters')])
    confirm = PasswordField('Password', [DataRequired(), EqualTo('password', 'Passwords is not equals'),
                                         length(6, 20, 'Password must be 6-20 characters')])
    register = SubmitField('Register')


class LoginForm(Form):
    email = StringField('Email', [DataRequired(), length(3, 30, 'Email must be 3-30 characters')])
    password = PasswordField('Password', [DataRequired(), length(6, 20, 'Password must be 6-20 characters')])
    login = SubmitField('Login')


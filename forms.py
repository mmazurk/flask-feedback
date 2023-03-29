from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length


class RegisterForm(FlaskForm):
    """form for user to register"""

    username = StringField('Enter a short username', validators=[InputRequired()])
    password = PasswordField('Enter Password', validators=[InputRequired()])
    email = StringField('Your Email Address')
    first_name = StringField('First Name')
    last_name = StringField('Last Name')


class LoginForm(FlaskForm):
    """form for a user to log in"""

    username = StringField('Username', validators=[InputRequired()])
    password = StringField('Password', validators=[InputRequired()])

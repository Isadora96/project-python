from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileField, FileAllowed

from flask_login import current_user
from hamburguerblog.models import User

class LoginForm(FlaskForm):

    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')

class RegistrationForm(FlaskForm):

    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('pass_confirm', message='Password must match!!')])
    pass_confirm = StringField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Register')

    @staticmethod
    def check_email(field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Your email has been registered already!')

    @staticmethod
    def check_username(field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('This username has been registered already!')


class UpdateUserForm(FlaskForm):

    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    @staticmethod
    def check_email(field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Your email has been registered already!')

    @staticmethod
    def check_username(field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('This username has been registered already!')


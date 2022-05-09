from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, ValidationError
from wtforms.validators import DataRequired, Length
from recipe_app.models import User
from recipe_app import bcrypt

class SignUpForm(FlaskForm):
    username = StringField('User Name',
        validators=[DataRequired(), Length(min=3, max=20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=3, max=20)])
    first_name = StringField('First Name',
        validators=[DataRequired(), Length(max=20)])
    last_name = StringField('Last Name',
        validators=[DataRequired(), Length(max=20)])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

class LoginForm(FlaskForm):
    username = StringField('User Name',
        validators=[DataRequired(), Length(min=3, max=50)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if not user:
            raise ValidationError('No user with that username. Please try again.')

    def validate_password(self, password):
        user = User.query.filter_by(username=self.username.data).first()
        if user and not bcrypt.check_password_hash(
                user.password, password.data):
            raise ValidationError('Password doesn\'t match. Please try again.')
        

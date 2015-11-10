from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email

class SignupForm(Form):
    first_name = StringField('First name', validators=[DataRequired("Please enter your first name.")])
    last_name = StringField('Last name', validators=[DataRequired("Please enter your last name.")])
    email = StringField('Email', validators=[DataRequired("Please enter a valid email address"), Email("Enter email in the format user@example.com")])
    password = PasswordField('Password', validators=[DataRequired("Please create a password")])
    submit = SubmitField('Sign up')

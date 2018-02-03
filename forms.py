from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Email, Length, NumberRange

class SignupForm(FlaskForm):
    first_name = StringField('First name', validators=[DataRequired("Put YO Name")])
    last_name = StringField('Last name', validators=[DataRequired("PUT YOUR LAST NAMAE")])
    email = StringField('Email', validators=[DataRequired("I won't spam you I promise"), Email("PUT A REAL EMAIL")])
    password = PasswordField('Password', validators=[DataRequired("DO IT"), Length(min=6, message="Think harder man")])
    submit = SubmitField('Sign up')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired("Please enter an email"), Email("put a real email")])
    password = PasswordField('Password', validators=[DataRequired("Enter your password")])
    submit = SubmitField("Sign in")

#apparently if it is listed here it must be used in the HTML otherwise it doesnt work. Removed unnecessary attributes
class PatientForm(FlaskForm):
    first_name = StringField('First name', validators=[DataRequired("Enter first name")])
    last_name = StringField('Last Name', validators=[DataRequired("Enter last name")])
    age = IntegerField('Age', validators=[DataRequired("Enter your age"), NumberRange(min=0, max=100, message="Enter an age between 0-100")])
    s_pulse = IntegerField('Starting Pulse', validators=[DataRequired("Enter your starting heart rate"), NumberRange(min=0)], description="Take starting pulse (count how many beats you get in 10 seconds then multiply by 6")
    e_pulse = IntegerField('Ending Pulse', validators=[DataRequired("Enter your ending heart rate"), NumberRange(min=0)], description="Take ending pulse immediately after exercise (count how many beats you get in 10 seconds then multiply by 6)" )
    submit = SubmitField('Complete')

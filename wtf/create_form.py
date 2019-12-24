from flask_wtf import *
from wtforms import *
class Createclass(Form):
    name=TextField("Name:",[validators.Required('Enter the name of the person')])
    email=TextField("Email",[validators.Required('Enter the email address')])
    work=RadioField("Status",choices=[('stu','Student'),('sta','Staff')])
    submit=SubmitField("go")
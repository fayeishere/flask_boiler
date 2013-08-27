
from wtforms import TextField, SubmitField, validators, TextAreaField, ValidationError
from flask.ext.wtf import Form
 

class ContactForm(Form):
	name = TextField("Name",  [validators.Required("Please enter your name.")])
	email = TextField("Email",  [validators.Required("Please enter your email address."), validators.Email("Please enter your email address.")])
	subject = TextField("Subject",  [validators.Required("Please enter a subject.")])
	message = TextAreaField("Message",  [validators.Required("Please enter a message.")])
	submit = SubmitField("Send")
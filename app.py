from flask import Flask, render_template, flash
from flask.ext.bootstrap import Bootstrap
from flask.ext.wtf import Form 
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import Required, Email

class ContactForm(Form):
	name = StringField('What is your name?', validators=[Required()])
	email = StringField('What is your email address?', validators=[Required(),Email()])
	msg = TextAreaField('What do you want to say to us?', validators=[Required()])
	submit = SubmitField('Submit')

app = Flask('__name__')
bootstrap = Bootstrap(app)
app.config['SECRET_KEY']='youcantguessthis'

@app.route('/', methods=['GET', 'POST'])
def index():
	form = ContactForm()
	if form.validate_on_submit():
		msgfile = open("msgs.txt","a")
		msgfile.write("Name:	"+form.name.data+"\n")
		msgfile.write("Email:	"+form.email.data+"\n")
		msgfile.write("Message:	"+form.msg.data+"\n\n\n")
		msgfile.close();
		flash('Thanks for submitting the form, we\'ll respond back soon')
		form.name.data=''
		form.email.data=''
		form.msg.data=''
	return render_template('index.html', form=form);

@app.route('/webmail')
def webmail():
	return render_template('webmail.html')

@app.route('/ebapps')
def ebapps():
	return render_template('ebapps.html')

@app.route('/msgs')
def msgs():
	msgfile = open('msgs.txt').readlines()
	output = ""
	for line in msgfile:
		output += line + "<br />"

	return output

#if __name__ == '__main__':
#	app.run(host='0.0.0.0',port=8000,debug=True)

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

'''class IndiForm(Form):
	name = StringField('Name', validators=[Required()])
	email = StringField('Email Address', validators=[Required(),Email()])
	school = StringField('School')		
	phone = StringField('Phone Number')		
	exp = TextAreaField('Previous MUN experience. Format: MUN - Position or Country - Committee - Prize Won', validators=[Required()])
	pref1 = StringField('Committee and Allotment preference 1', validators=[Required()])
	pref2 = StringField('Committee and Allotment preference 2', validators=[Required()])
	pref3 = StringField('Committee and Allotment preference 3')
	submit = SubmitField('Submit')
'''
app = Flask('__name__')
bootstrap = Bootstrap(app)
app.config['SECRET_KEY']='youcantguessthis'

@app.route('/', methods=['GET', 'POST'])
def index():
	form = ContactForm()
	#delform  = IndiForm()
	if form.validate_on_submit():
		msgfile = open("msgs.txt","a")
		
		msgfile.write("Name:	"+form.name.data+"\n")
		msgfile.write("Email:	"+form.email.data+"\n")
		msgfile.write("Message:	"+form.msg.data+"\n")
		msgfile.write("-------------------------------------------------------------\n\n")
		msgfile.close();
		flash('Thanks for submitting the form, we\'ll respond back soon')
		form.name.data=''
		form.email.data=''
		form.msg.data=''

	'''if delform.validate_on_submit():
		delfile = open("applications.txt","a")
		delfile.write("Name:	"+delform.name.data+"\n")
		delfile.write("Email:	"+delform.email.data+"\n")
		delfile.write("School:	"+delform.school.data+"\n")
		delfile.write("Phone:	"+delform.phone.data+"\n")
		delfile.write("Experience:	"+delform.exp.data+"\n")
		delfile.write("Preference 1:	"+delform.pref1.data+"\n")
		delfile.write("Preference 2:	"+delform.pref2.data+"\n")
		delfile.write("Preference 3:	"+delform.pref3.data+"\n")
		delfile.write("-------------------------------------------------------------\n\n")
		delfile.close();
		flash('Thanks for submitting the application, we\'ll respond back soon and confirm you via mail.')
		delform.name.data=''
		delform.email.data=''
		delform.school.data=''
		delform.phone.data=''
		delform.exp.data=''
		delform.pref1.data=''
		delform.pref2.data=''
		delform.pref3.data=''
'''
	return render_template('index.html', form=form)

@app.route('/webmail')
def webmail():
	return render_template('webmail.html')

'''@app.route('/ebapps')
def ebapps():
	return render_template('ebapps.html')
'''
@app.route('/msgs')
def msgs():
	msgfile = open('msgs.txt').readlines()
	output = ""
	for line in msgfile:
		output += line + "<br />"

	return output

@app.route('/applications')
def applications():
	delfile = open('applications.txt').readlines()
	output = ""
	for line in delfile:
		output += line + "<br />"

	return output

@app.route('/alfaaz', methods=['GET','POST'])
def newsletters():
	form = ContactForm()
	if form.validate_on_submit():
		msgfile = open("msgs.txt","a")
		
		msgfile.write("Name:	"+form.name.data+"\n")
		msgfile.write("Email:	"+form.email.data+"\n")
		msgfile.write("Message:	"+form.msg.data+"\n")
		msgfile.write("-------------------------------------------------------------\n\n")
		msgfile.close();
		flash('Thanks for submitting the form, we\'ll respond back soon')
		form.name.data=''
		form.email.data=''
		form.msg.data=''
	return render_template('blog.html',form=form)

@app.route('/issue-1')
def alfaaz1():
	return '''
	<iframe style="width:100%; height:100%;" src="//e.issuu.com/embed.html#27549567/42432229" frameborder="0" allowfullscreen></iframe>'''

@app.route('/issue-2')
def alfaaz2():
	return "something";

@app.route('/issue-3')
def alfaaz3():
	return "will be up";


@app.route('/issue-4')
def alfaaz4():
	return "will be up";
	
if __name__ == '__main__':
	app.run(host='0.0.0.0',port=8000,debug=True)

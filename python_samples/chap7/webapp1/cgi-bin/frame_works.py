#! /usr/local/bin/python3

import cgitb

def startHtml():
	return "<html>"
def endHtml():
	return "</html>"
def header():
	return "<head></head>"
def body(content):	
	return "<body>"+content+"</body>"
def prepareSubmitForm(value, method='POST'):
	return "<input type='submit' value='"+value+"' method='"+method+"'>"
def prepareTextForm(identifier,name,type):
	return identifier+ " : <input name='"+name+"' type='"+type+"'>"
def prepareForm(forms,action_script):
	full_form = "<form action='"+action_script+"'>"
	for form in forms:
		full_form = full_form + "<br/>" + form
	return full_form+"</form>"

cgitb.enable()

print("Content-type:text/html\n\n")
print(startHtml())
print(header())
forms = []
forms.append(prepareTextForm("First Name","firstname","text"))
forms.append(prepareTextForm("Middle Name","middlename","text"))
forms.append(prepareTextForm("Last Name","lastname","text"))
forms.append(prepareSubmitForm("submit"))
print(body(prepareForm(forms,"action.py")))
print(endHtml())
#print("cde")
#! /usr/local/bin/python3
import cgi
import cgitb

cgitb.enable()
form_data = cgi.FieldStorage()
fname = ""
mname = ""
lname = ""
if 'firstname' in form_data:
	fname = form_data['firstname'].value
if 'middlename' in form_data:
	mname = form_data['middlename'].value
if 'lastname' in form_data:
	lname = form_data['lastname'].value
print("Content-type:text/html\n\n")
print("<html><head></head><body> Name Entered : "+str(fname) +" "+str(mname)+" "+str(lname)+"</body></html>")
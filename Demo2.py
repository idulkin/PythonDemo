import webapp2
import re
'''
USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PW_RE = re.compile(r"^.{3,20}$")
EMAIL_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$"
'''
form="""
<form method="post">
    <b><font size="20">Signup</font></b>
    <br>
    
    <label>
	&nbsp;        Username
	<input type="text" name="username" value="%(username)s">
	<div style="color: red">%(unError)s</div>
    </label>
    <br>
    <label>
	 &nbsp;       Password
	<input type="password" name="password" value="%(password)s">
	<div style="color: red">%(pwError)s</div>
    </label>
    <br>
    <label>
	&nbsp; Verify Password
	<input type="password" name="vpassword" value="%(vpassword)s">
	<div style="color: red">%(valError)s</div>
    </label>
    <br>
    <label>
	 &nbsp; Email(optional)
	<input type="text" name="email" value="%(email)s">
	<div style="color: red">%(emError)s</div>
    </label>
    <br>
     
   
    <input type="submit">
    <input type="reset">
</form>	
"""

class MainPage(webapp2.RequestHandler):

    USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
    PW_RE = re.compile(r"^.{3,20}$")
    EMAIL_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$"

    def writeForm(self,username="",password="",vpassword="",email="",unError="",pwError="",valError="",emError=""):
        self.response.out.write(form %{"username": username,
				       "password": password,
				       "vpassword": vpassword,
				       "email": email,
				       "unError": unError,
				       "pwError": pwError,
				       "valError": valError,
				       "emError": emError})
    def get(self):
	self.writeForm()
    
    def post(self):
        inUsername = self.request.get("username")
        inPassword = self.request.get("password")
        inValidation= self.request.get("vpassword")
        inEmail= self.request.get("email")
        
        if(USER_RE.match(username)):
            erUsername = "Invalid username"
        
        self.writeForm(inUsername,inPassword,inValidation,inEmail,erUsername)


app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)


print("Hello worgle.")

import webapp2
import re

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
        self.writeForm("That's a terrible username")


app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)


print("Hello worgle.")

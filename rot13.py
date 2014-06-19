import webapp2

form="""
<form method="post" action='/rot13' name="myForm">
    <textarea cols="50" rows="25" name="text">%(code)s
    </textarea>
    <br>
    <input type="submit">
    <input type="reset">
</form>	
"""

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(form %{'code':""})

class Cypher(webapp2.RequestHandler):
    def writeForm(self,value):
	self.response.out.write(form %{'code': value})

    def post(self):
	out = self.request.get('text')
	out = out.encode("rot13")
        self.writeForm(out)


app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/rot13',Cypher),
], debug=True)


print("Hello worgle.")

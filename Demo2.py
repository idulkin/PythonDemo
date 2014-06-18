import webapp2

form="""
<form method="post" action='/rot13'>
    <textarea cols="50" rows="25" name="text">
    </textarea>
    <br>
    <input type="submit">
    <input type="reset">
</form>	
"""

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(form)

class Cypher(webapp2.RequestHandler):
    def writeForm(self,text):
	self.response.out.write(form %{"text": text})

    def post(self):
	out = self.request.get('text')
        self.writeForm(text=out)
	self.response.out.write(out)


app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/rot13',Cypher),
], debug=True)


print("Hello worgle.")

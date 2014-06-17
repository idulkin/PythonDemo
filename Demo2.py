import webapp2

form="""
<form method="get" action="/">
    <textarea cols="50" rows="5" name="cypherfield">
    </textarea>
    <br>
    <input type="submit">
    <input type="reset">
</form>	
"""

class MainPage(webapp2.RequestHandler):
    def writeForm(self, cypherfield=""):
        self.response.out.write(form %{"cyperfield":cypherfield})

    def get(self):
        #self.response.headers['Content-Type'] = 'text/plain'
        self.writeForm()

    def post(self):
        c = self.request.get('cypherfield')
        self.writeForm(c)
        self.response.out.write(c)
        self.response.out.write(" Words")

class Cypher(webapp2.RequestHandler):
    def get(self):
        c = self.request.get('cypherfield')
        self.reponse.out.write(c)
        self.response.out.write(" Words")
'''    
class TestHandler(webapp2.RequestHandler):
    def get(self):
	q = self.request.get("q")
	self.response.out.write(q)
	self.response.out.write("Worgle")
'''
app = webapp2.WSGIApplication([('/', MainPage)
			     ('/rot13',Cypher)],
                              debug=True)


print("Hello worgle.")

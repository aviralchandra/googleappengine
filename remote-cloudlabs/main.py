import webapp2
from google.appengine.ext import db

class MyData(db.Model):
	temp = db.IntegerProperty()
	heat = db.IntegerProperty()
	fan = db.IntegerProperty()

class HelloWorld(webapp2.RequestHandler):
	def get(self):
		temp = self.request.get('temp')
		heat = self.request.get('heat')
		fan = self.request.get('fan')
		data = MyData()
		data.temp = int(temp)
		data.heat = int(heat)
		data.fan = int(fan)
		data.put()

class Fetcher(webapp2.RequestHandler):
	def get(self):
		data = db.GqlQuery("select * from MyData")	
		
		for x in data:
			str = "TEMP= %d, HEAT=%d, FAN=%d <br>" %(x.temp,x.heat,x.fan)
			self.response.write(str)

app = webapp2.WSGIApplication([
	('/hello', HelloWorld),
	('/display', Fetcher)
], debug=True)

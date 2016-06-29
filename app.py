import tornado.ioloop
import tornado.web
import tornado.httpserver

import os.path

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')


class FormHandler(tornado.web.RequestHandler):
	def get(self):
		self.render('form.html')
	def post(self):
		owner, business = {},{}
		for element in self.request.arguments.keys():
			if 'owner' in element:
				owner[element]=self.request.arguments[element][0]
			elif 'business' in element:
				business[element]=self.request.arguments[element][0]

		#owner db insert
		#db = database.Connection("localhost", "mydatabase")
		#db.query("INSERT INTO owner (social_number, name, email, address, city,state,postal)
		#VALUES (owner['social_number'], owner['name'], owner['email'], owner['address'], 
		#owner['city'],owner['state'],owner['postal'])")

		#owner db insert
		#db.query("SELECT * FROM articles")
		#db.close()
    
		amount = float(self.get_argument('amount'))
		if amount < 50000:
			state = 'Aproved'
		elif amount == 50000:
			state = 'Undecided'
		else:
			state = 'Declined'
		context = self.get_template_namespace()
		context['state']=state
		self.render("summary.html", **context)		


class SummaryHandler(tornado.web.RequestHandler):
	def get(self):
		self.render('summary.html')


settings = dict(
         template_path = os.path.join(os.path.dirname(__file__), 'templates'),
         static_path = os.path.join(os.path.dirname(__file__), 'static'),
         debug = True,                  
)

application = tornado.web.Application([
    (r"/",MainHandler),
    (r"/form",FormHandler),
    (r"/summary",SummaryHandler),
],**settings)

if __name__ == '__main__':
    print "server is running"
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(5000)    
    tornado.ioloop.IOLoop.instance().start()

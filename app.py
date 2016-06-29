import tornado.ioloop
import tornado.web
import tornado.httpserver
import os
from settings import *

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        context = {}
        context['TITLE']='Welcome to Lendingfront'
        self.render('index.html', **context)


class FormHandler(tornado.web.RequestHandler):
    def get(self):
        context = {}
        context['TITLE']='Application form'
        self.render('form.html', **context)
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
        #db.close()       
    
        amount = float(self.get_argument('amount'))
        if amount < 50000:
            state = 'Aproved'
        elif amount == 50000:
            state = 'Undecided'
        else:
            state = 'Declined'
        context = self.get_template_namespace()
        context['state'] = state
        context['owner'] = owner['owner-name']
        context['business'] = business['business-name']
        context['TITLE'] = 'Summary'
        self.render("summary.html", **context)      


class SummaryHandler(tornado.web.RequestHandler):
    def get(self):
        context = {}
        context['TITLE']='Summary'
        self.render('form.html', **context)
        self.render('summary.html')

APP = tornado.web.Application([
    (r"/",MainHandler),
    (r"/form",FormHandler),
    (r"/summary",SummaryHandler),
],**SETTINGS)

if __name__ == '__main__':
    print "server is running"
    http_server = tornado.httpserver.HTTPServer(APP)
    http_server.listen(PORT)    
    tornado.ioloop.IOLoop.instance().start()

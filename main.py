#!/usr/bin/env python
import webapp2
import jinja2
import os

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainHandler(webapp2.RequestHandler):
    def get(self,page):
        template_values={}
        if page not in ('andrew',):
            page='front'
        template = JINJA_ENVIRONMENT.get_template(page+'.html')
        self.response.write(template.render(template_values))
        
app = webapp2.WSGIApplication([
    ('/([^/]+)?', MainHandler),
], debug=True)


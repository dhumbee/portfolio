import webapp2
import os

import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'html')
jinja_env = jinja2.Environment(autoescape=True, loader = jinja2.FileSystemLoader(template_dir))

class myHandler(webapp2.RequestHandler):
	def write(self, *a, **kw):
		self.response.write(*a, **kw)

	def render_str(self, template, **params):
		template = jinja_env.get_template(template)
		return template.render(params)

	def render(self, template, **kw):
		self.write(self.render_str(template,**kw))

class MainPage(myHandler):
	def get(self):
		self.render ("portfolio.html")

application=webapp2.WSGIApplication([('/', MainPage)])		
#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os
import jinja2
import webapp2

from google.appengine.ext import ndb

JINJA_ENVIRONMENT = jinja2.Environment(
	loader=jinja2.FileSystemLoader(os.path.dirname( __file__ )),
	extensions = ["jinja2.ext.autoescape"],
	autoescape = True
)

class Tip(ndb.Model):
	cif = ndb.StringProperty(required = True)
	nameCompany = ndb.StringProperty(required = True)
	dni = ndb.StringProperty(required = True)
	nameClient = ndb.StringProperty(required = True)
	lines = ndb.StringProperty(repeated = True)

class TipsHandler(webapp2.RequestHandler):
	def __init__(self, request = None, response = None):
		self.initialize(request, response)

	def load_input(self):
		self.cif = self.request.get('cif', 'anonymous')
		self.nameCompany = self.request.get('nameCompany', 'anonymous')
		self.dni = self.request.get('dni', 'anonymous')
		self.nameClient = self.request.get('nameClient', 'anonymous')

		self.clicks = self.request.get('clicks', 0)

		self.lines = list()

		for i in range(int(self.clicks)):
			self.lines.append(self.request.get(str(i)))

	def save(self):
		tip = Tip(cif = self.cif, nameCompany = self.nameCompany, dni = self.dni, nameClient = self.nameClient, lines = self.lines)
		tip.put()

	def post(self):
		self.load_input()
		self.save()

		query = Tip.query().order(Tip.nameCompany)

		template_values = {
			'tip' : query
		}

		template = JINJA_ENVIRONMENT.get_template('output.html')
		self.response.write(template.render(template_values))

app = webapp2.WSGIApplication([
('/save', TipsHandler),
], debug=True)

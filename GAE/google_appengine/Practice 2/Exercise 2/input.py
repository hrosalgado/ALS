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

JINJA_ENVIRONMENT = jinja2.Environment(
	loader=jinja2.FileSystemLoader(os.path.dirname( __file__ )),
	extensions = ["jinja2.ext.autoescape"],
	autoescape = True
)

class TipsHandler(webapp2.RequestHandler):
	def __init__(self, request=None, response=None):
		self.initialize(request, response)

		self.cif1 = self.request.get('cif1')
		self.name1 = self.request.get('name1')
		self.address1 = self.request.get('address1')
		self.city1 = self.request.get('city1')
		self.province1 = self.request.get('province1')
		self.cp1 = self.request.get('cp1')
		self.country1 = self.request.get('country1')
		self.contactPerson1 = self.request.get('contactPerson1')
		self.mail1 = self.request.get('mail1')
		self.phone1 = self.request.get('phone1')

		self.cif2 = self.request.get('cif2')
		self.name2 = self.request.get('name2')
		self.address2 = self.request.get('address2')
		self.city2 = self.request.get('city2')
		self.province2 = self.request.get('province2')
		self.cp2 = self.request.get('cp2')
		self.country2 = self.request.get('country2')
		self.contactPerson2 = self.request.get('contactPerson2')
		self.mail2 = self.request.get('mail2')
		self.phone2 = self.request.get('phone2')

		self.concept = self.request.get('concept')
		self.pricePerUnit = self.request.get('pricePerUnit')
		self.units = self.request.get('units')
		self.firstCost = self.request.get('firstCost')
		self.iva = self.request.get('iva')
		self.lastCost = self.request.get('lastCost')
		
	def post(self):
		flag = False
		for key, value in self.request.POST.items():
			if value == '':
				flag = True
				break

		if flag:
			self.redirect('http://localhost:8080')
		else:
			template_values = {
				'cif1' : self.cif1,
				'name1' : self.name1,
				'address1' : self.address1,
				'city1' : self.city1,
				'province1' : self.province1,
				'cp1' : self.cp1
				'country1' : self.country1
				'contactPerson1' : self.contactPerson1
				'mail1' : self.mail1
				'phone1' : self.phone1

				: self.cif2
				: self.name2
				: self.address2
				: self.city2,
				: self.province2,
				: self.cp2,
				: self.country2,
				: self.contactPerson2,
				: self.mail2,
				: self.phone2,

				: self.concept,
				: self.pricePerUnit,
				: self.units,
				: self.firstCost,
				: self.iva,
				: self.lastCost,
			}
			self.response.write('OK')

app = webapp2.WSGIApplication([
('/tip', TipsHandler),
], debug=True)

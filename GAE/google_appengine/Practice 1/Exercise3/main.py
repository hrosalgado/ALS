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
import webapp2
import re

class MainHandler(webapp2.RequestHandler):
	def __init__(self, request = None, response = None):
		self.initialize(request, response)
		self.temperature = self.request.get('temperature', 'anonymous')

	def post(self):
		if re.match('^[0-9]+(.[0-9]+)*$', self.temperature) == None:
			self.redirect('localhost:8080')
		else:
			celsius = int(self.temperature) + 1
			farenheit = int(self.temperature) * 1.8 + 32
			self.response.write('Celsius: ' + str(celsius) + ' , Farenheit: ' + str(farenheit))		

app = webapp2.WSGIApplication([
	('/convert', MainHandler)
], debug=True)

from requests import post
from requests.auth import HTTPBasicAuth

from .functions import Contact, Task


class PlanfixAPI(object):
	account = None
	token = None
	api_key = None 

	url = 'https://api.planfix.ru/xml'
	headers = {'Accept': 'application/xml', 'Content-Type': 'application/xml'}

	def __init__(self, account=None, token=None, api_key=None):
		self.account = account
		self.token = token
		self.api_key = api_key

		self.task = Task(self)
		self.contact = Contact(self)

	def _send_request(self, xml):
		response = post(
				self.url, 
				data=xml.encode('UTF-8'), 
				headers=self.headers, 
				auth=HTTPBasicAuth(
						self.api_key,
						self.token, 
					)
			)

		text = response.text
		return text

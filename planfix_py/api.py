from requests import post
from requests.auth import HTTPBasicAuth

from jinja2 import Environment, PackageLoader

from .functions import Contact, Task


class PlanfixAPI(object):
	account = None
	token = None
	api_key = None 

	url = 'https://api.planfix.ru/xml'
	headers = {'Accept': 'application/xml', 'Content-Type': 'application/xml'}

	__templates_env = Environment(
			loader=PackageLoader('planfix_py', 'templates')
		)

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

	def _load_template(self, template_name, *args, **kwargs):
		template = self.__templates_env.get_template(template_name)
		request_message = template.render(**kwargs)

		return request_message

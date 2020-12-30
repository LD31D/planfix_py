from requests import post
from requests.auth import HTTPBasicAuth


class PlanfixAPI(object):
	_URL = 'https://api.planfix.ru/xml'
	_HEADERS = {'Accept': 'application/xml', 'Content-Type': 'application/xml'}

	def __init__(self, account=None, token=None, api_key=None):
		self._account = account
		self._token = token
		self._api_key = api_key

	def _send_request(self, xml):
		response = post(
				self._URL, 
				data=xml.encode('UTF-8'), 
				headers=self._HEADERS, 
				auth=HTTPBasicAuth(
						self._api_key,
						self._token, 
					)
			)

		text = response.text
		return text

class PlanfixAPI(object):
	_URL = 'https://api.planfix.ru/xml'
	_HEADERS = {'Accept': 'application/xml', 'Content-Type': 'application/xml'}

	def __init__(self, account=None, token=None, api_key=None):
		self._account = account
		self._token = token
		self._api_key = api_key

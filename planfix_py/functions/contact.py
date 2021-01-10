class Contact(object):

	TEMPLATE_FOLDER = 'contact/'
	
	def __init__(self, base):
		self.__base__ = base

	def add(self, *args, **kwargs):
		"""
		https://planfix.ru/docs/%D0%9F%D0%BB%D0%B0%D0%BD%D0%A4%D0%B8%D0%BA%D1%81_API_contact.add
		"""
		TEMPLATE_NAME = self.TEMPLATE_FOLDER + 'add.xml'

		kwargs['account'] = self.__base__.account

		request_message = self.__base__._load_template(TEMPLATE_NAME, **kwargs)
		# print(request_message)
		response = self.__base__._send_request(request_message)

		return response

	def update(self):
		"""
		https://planfix.ru/docs/%D0%9F%D0%BB%D0%B0%D0%BD%D0%A4%D0%B8%D0%BA%D1%81_API_contact.update
		"""
		pass

	def update_custom_data(self):
		"""
		https://planfix.ru/docs/%D0%9F%D0%BB%D0%B0%D0%BD%D0%A4%D0%B8%D0%BA%D1%81_API_contact.updateCustomData
		"""
		pass

	def get(self):
		"""
		https://planfix.ru/docs/%D0%9F%D0%BB%D0%B0%D0%BD%D0%A4%D0%B8%D0%BA%D1%81_API_contact.get
		"""
		pass

	def get_list(self):
		"""
		https://planfix.ru/docs/%D0%9F%D0%BB%D0%B0%D0%BD%D0%A4%D0%B8%D0%BA%D1%81_API_contact.getList
		"""
		pass

	def manage_planfix_access(self):
		"""
		https://planfix.ru/docs/%D0%9F%D0%BB%D0%B0%D0%BD%D0%A4%D0%B8%D0%BA%D1%81_API_contact.managePlanfixAccess
		"""
		pass

	def update_user_info(self):
		"""
		https://planfix.ru/docs/%D0%9F%D0%BB%D0%B0%D0%BD%D0%A4%D0%B8%D0%BA%D1%81_API_contact.updateUserInfo
		"""
		pass

	def update_contractors(self):
		"""
		https://planfix.ru/docs/%D0%9F%D0%BB%D0%B0%D0%BD%D0%A4%D0%B8%D0%BA%D1%81_API_contact.updateContractors
		"""
		pass

	def get_phone_types(self):
		"""
		https://planfix.ru/docs/%D0%9F%D0%BB%D0%B0%D0%BD%D0%A4%D0%B8%D0%BA%D1%81_API_contact.getPhoneTypes
		"""
		pass

	def get_group_list(self):
		"""
		https://planfix.ru/docs/%D0%9F%D0%BB%D0%B0%D0%BD%D0%A4%D0%B8%D0%BA%D1%81_API_contact.getGroupList
		"""
		pass

	def delete(self):
		"""
		https://planfix.ru/docs/%D0%9F%D0%BB%D0%B0%D0%BD%D0%A4%D0%B8%D0%BA%D1%81_API_contact.delete
		"""
		pass
		
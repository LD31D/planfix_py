class Contact(object):

	TEMPLATE_FOLDER = 'contact/'
	
	def __init__(self, base):
		self.__base__ = base

	def add(self, kwargs):
		"""
		https://planfix.ru/docs/%D0%9F%D0%BB%D0%B0%D0%BD%D0%A4%D0%B8%D0%BA%D1%81_API_contact.add
		"""
		TEMPLATE_NAME = self.TEMPLATE_FOLDER + 'add.xml'

		response = self.__base__._get_response(TEMPLATE_NAME, kwargs)

		return response

	def update(self, kwargs):
		"""
		https://planfix.ru/docs/%D0%9F%D0%BB%D0%B0%D0%BD%D0%A4%D0%B8%D0%BA%D1%81_API_contact.update
		"""
		TEMPLATE_NAME = self.TEMPLATE_FOLDER + 'update.xml'

		response = self.__base__._get_response(TEMPLATE_NAME, kwargs)

		return response 

	def update_custom_data(self, kwargs):
		"""
		https://planfix.ru/docs/%D0%9F%D0%BB%D0%B0%D0%BD%D0%A4%D0%B8%D0%BA%D1%81_API_contact.updateCustomData
		"""
		TEMPLATE_NAME = self.TEMPLATE_FOLDER + 'updateCustomData.xml'

		response = self.__base__._get_response(TEMPLATE_NAME, kwargs)

		return response

	def get(self):
		"""
		https://planfix.ru/docs/%D0%9F%D0%BB%D0%B0%D0%BD%D0%A4%D0%B8%D0%BA%D1%81_API_contact.get
		"""
		TEMPLATE_NAME = self.TEMPLATE_FOLDER + 'get.xml'

		response = self.__base__._get_response(TEMPLATE_NAME, kwargs)

		return response

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
		
import unittest
from collections import OrderedDict

from planfix_py import PlanfixAPI


class TestContact(unittest.TestCase):

	COMING_RESPONSE = OrderedDict([('response', OrderedDict([('@status', 'error'), ('code', '0001'), ('message', None)]))])

	def setUp(self):
		self.pf = PlanfixAPI()

	def test_contact_add(self):
		response = self.pf.contact.add({})

		self.assertEqual(self.COMING_RESPONSE, response)

	def test_contact_update(self):
		response = self.pf.contact.update({})

		self.assertEqual(self.COMING_RESPONSE, response)

	def test_contact_update_custom_data(self):
		response = self.pf.contact.update_custom_data({})

		self.assertEqual(self.COMING_RESPONSE, response)

	def test_contact_get(self):
		response = self.pf.contact.get({})

		self.assertEqual(self.COMING_RESPONSE, response)

	def test_contact_get_list(self):
		response = self.pf.contact.get_list({})

		self.assertEqual(self.COMING_RESPONSE, response)

	def test_contact_manage_planfix_access(self):
		response = self.pf.contact.manage_planfix_access({})

		self.assertEqual(self.COMING_RESPONSE, response)

	def test_contact_update_user_info(self):
		response = self.pf.contact.update_user_info({})

		self.assertEqual(self.COMING_RESPONSE, response)

	def test_contact_update_contractors(self):
		response = self.pf.contact.update_contractors({})

		self.assertEqual(self.COMING_RESPONSE, response)

	def test_contact_get_phone_types(self):
		response = self.pf.contact.get_phone_types({})

		self.assertEqual(self.COMING_RESPONSE, response)

	def test_contact_get_group_list(self):
		response = self.pf.contact.get_group_list({})

		self.assertEqual(self.COMING_RESPONSE, response)

	def test_contact_delete(self):
		response = self.pf.contact.delete({})

		self.assertEqual(self.COMING_RESPONSE, response)


if __name__ == '__main__':
	unittest.main()
	
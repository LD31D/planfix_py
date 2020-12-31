import unittest
import pkg_resources  # part of setuptools

from requests import get


class TestPYPI(unittest.TestCase):

    def test_version(self):
    	package_version = pkg_resources.get_distribution("planfix-py").version
    	
    	url = f'https://pypi.org/project/planfix-py/{package_version}/'
    	response = get(url)

    	self.assertIn('Error code 404', response.text)


if __name__ == '__main__':
    unittest.main()
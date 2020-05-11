# my_pages_app/tests.py

# DEFAULT IS from django.test import TestCase
from django.test import SimpleTestCase  # does not provide a database - we don't need

class SimpleTests(SimpleTestCase):
	""" """

	def test_home_page_status_code(self):
		""" check the status code returned from rendering HOME page """
		response = self.client.get("/")
		self.assertEqual(response.status_code, 200)

		response = self.client.get("/home/")
		self.assertEqual(response.status_code, 200)


	def test_about_page_status_code(self):
		""" check the status code returned from rendering HOME page """
		# NOTE 'about/', "/about", and "about" return error codes 301, 404
		response = self.client.get("/about/")
		self.assertEqual(response.status_code, 200)



### end ###

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class SampleTest(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Firefox()
		self.driver.get("https://www.google.com/?gws_rd=ssl")


	def test_google_title(self):
		assert "Google" in self.driver.title


	def tearDown(self):
		self.driver.close()
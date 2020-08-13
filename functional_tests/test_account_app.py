# from selenium import webdriver
# from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
# from selenium.webdriver.common.keys import Keys
# from django.contrib.staticfiles.testing import StaticLiveServerTestCase
# from django.urls import reverse
# import os
# import time

# from Food.models import Product, Ingredient, ReceipeIngredient


# class TestAccountApp(StaticLiveServerTestCase):

# 	def __init__(self, methodName='runTest'):
# 		self.server_url = "http://127.0.0.1:8000"
# 		super(TestAccountApp, self).__init__(methodName)

# 	def setUp(self):
# 		# self.webdriver = webdriver.Chrome(executable_path="functional_tests/chromedriver.exe")
# 		self.gecko = os.path.normpath(os.path.join(os.path.dirname(__file__), 'geckodriver'))
# 		self.webdriver = webdriver.Firefox(
# 				firefox_binary=FirefoxBinary(r"C:\Program Files (x86)\Mozilla Firefox\firefox.exe"),
# 				executable_path=self.gecko+".exe"
# 			)


# 	def test_log_in_form_displayed(self):			
# 		self.webdriver.get(self.server_url)
# 		alert = self.webdriver.find_element_by_link_text("Login").click()

# 		self.assertEquals(
# 				self.webdriver.current_url,
# 				self.server_url + reverse("profile:log_in")
# 			)


# 	def test_login_in(self):
# 		#self.webdriver.get(self.live_server_url)
# 		self.webdriver.get(self.server_url)
# 		self.webdriver.find_element_by_id("user_log_in").click()
# 		self.webdriver.find_element_by_id("id_username").send_keys("admin")
# 		self.webdriver.find_element_by_id("id_password").send_keys("admin")
# 		self.webdriver.find_element_by_id("id_password").send_keys(Keys.ENTER)
# 		time.sleep(2)
# 		self.assertEquals(
# 				self.webdriver.current_url,
# 				self.server_url + reverse("profile:profile_details")
# 			)


# 	def tearDown(self):
# 		self.webdriver.close()
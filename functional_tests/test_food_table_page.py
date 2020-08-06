from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
import time

from Food.models import Product, Ingredient, ReceipeIngredient

class TestProductTablePage(StaticLiveServerTestCase):

	def setUp(self):
		self.browser = webdriver.Chrome("functional_tests/chromedriver.exe")

	

	def test_no_projects_allerts_is_displayed(self):	
		self.browser.get(self.live_server_url)
		#time.sleep(3)
		#User visits page for the first time
		alert = self.browser.find_element_by_class_name("home")
		self.assertEquals(
				alert.find_element_by_tag_name("h3").text,
				"Welcome!"
			)

	def test_log_in_form_displayed(self):	
		self.browser.get(self.live_server_url)
		alert = self.browser.find_element_by_link_text("Login").click()

		self.assertEquals(
				self.browser.current_url,
				self.live_server_url + reverse("profile:log_in")
			)

	def test_product_table_displayed(self):	
		self.browser.get(self.live_server_url)
		alert = self.browser.find_element_by_link_text("Food").click()

		self.assertEquals(
			alert.find_element_by_tag_name("a").text,
			"product table"
		)

		# self.assertEquals(
		# 		self.browser.current_url,
		# 		self.live_server_url + reverse("food:prod_table")
		# 	)




	def tearDown(self):
		self.browser.close()



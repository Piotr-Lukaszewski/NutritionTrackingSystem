from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
import os
import time


from Food.models import Product, Ingredient, ReceipeIngredient

def test_log_in_user(func):
	def wrapper(self, *args, **kwargs):
		self.webdriver.get(self.local_host + reverse("profile:log_in"))
		username = self.webdriver.find_element_by_id("id_username")
		time.sleep(2)
		username.send_keys("admin")
		password = self.webdriver.find_element_by_id("id_password")
		time.sleep(2)
		password.send_keys("admin")
		time.sleep(2)
		password.send_keys(Keys.ENTER)
		time.sleep(3)
		func(self, *args, **kwargs)
	return wrapper

class TestProductTablePage(StaticLiveServerTestCase):


	def setUp(self):
		# self.webdriver = webdriver.Chrome(executable_path="functional_tests/chromedriver.exe")
		self.gecko = os.path.normpath(os.path.join(os.path.dirname(__file__), 'geckodriver'))
		self.webdriver = webdriver.Firefox(
				firefox_binary=FirefoxBinary(r"C:\Program Files (x86)\Mozilla Firefox\firefox.exe"),
				executable_path=self.gecko+".exe"
			)
		self.test_name = "Milk 2.0"
		self.local_host = "http://127.0.0.1:8000"

	def test_no_projects_allerts_is_displayed(self):	
		#User visits page for the first time
		self.webdriver.get(self.live_server_url)		
		alert = self.webdriver.find_element_by_class_name("home")
		self.assertEquals(
				alert.find_element_by_tag_name("h3").text,
				"Welcome!"
			)
	def test_product_table_search(self): 
		self.webdriver.get(self.local_host + "/food/prod_table/")
		self.webdriver.find_element_by_css_selector("input").send_keys(self.test_name)
		time.sleep(1)
		self.webdriver.find_element_by_css_selector("input").send_keys(Keys.ENTER)
		time.sleep(1)
		self.assertEquals(
				self.webdriver.find_element_by_id("fat").text,
				"2.0"
			)
		self.assertEquals(
				self.webdriver.find_element_by_id("product_name").text,
				self.test_name
			)
		self.assertEquals(
				self.webdriver.current_url,
				"http://127.0.0.1:8000" +\
				reverse("food:search_results") +\
				"?word=" +\
				self.test_name.replace(" ", "+")
			)

	@test_log_in_user
	def test_ingredient_creation(self):
		time.sleep(1)
		self.webdriver.find_element_by_link_text("Ingredients").click()
		self.webdriver.find_element_by_id("ingredient_creation").click()
		ingredinet_name = self.webdriver.find_element_by_id("id_name")
		ingredinet_name.send_keys("test")
		time.sleep(2)
		ingredinet_protein = self.webdriver.find_element_by_id("id_protein")
		ingredinet_protein.send_keys(10)	
		time.sleep(2)
		ingredinet_carbohydrates = self.webdriver.find_element_by_id("id_carbohydrates")
		ingredinet_carbohydrates.send_keys(20)
		time.sleep(2)
		ingredinet_fat = self.webdriver.find_element_by_id("id_fat")
		ingredinet_fat.send_keys(30)
		time.sleep(2)
		ingredinet_weight = self.webdriver.find_element_by_id("id_quantity_per_portion")
		ingredinet_weight.send_keys(99)
		time.sleep(2)
		ingredinet_price = self.webdriver.find_element_by_id("id_price")
		ingredinet_price.send_keys("1.99")
		food_type = self.webdriver.find_element_by_xpath("//*[@id='id_food_type']/option[2]")
		food_type.click()

	def tearDown(self):
		self.webdriver.close()



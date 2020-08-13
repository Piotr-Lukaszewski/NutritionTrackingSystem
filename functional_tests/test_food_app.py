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


class TestProductApp(StaticLiveServerTestCase):


	def __init__(self, methodName="runTest"):
		self.test_name_ingredient = "Milk 2.0"
		self.test_new_name_ingredient = "test"
		self.test_new_name_product = "Schabowy"		
		self.local_host = "http://127.0.0.1:8000"
		super(TestProductApp, self).__init__(methodName)


	def setUp(self):
		# self.webdriver = webdriver.Chrome(executable_path="functional_tests/chromedriver.exe")
		self.gecko = os.path.normpath(os.path.join(os.path.dirname(__file__), 'geckodriver'))
		self.webdriver = webdriver.Firefox(
				firefox_binary=FirefoxBinary(r"C:\Program Files (x86)\Mozilla Firefox\firefox.exe"),
				executable_path=self.gecko+".exe"
			)


	# def test_no_projects_allerts_is_displayed(self):	
	# 	#User visits page for the first time
	# 	self.webdriver.get(self.live_server_url)		
	# 	alert = self.webdriver.find_element_by_class_name("home")
	# 	self.assertEquals(
	# 			alert.find_element_by_tag_name("h3").text,
	# 			"Welcome!"
	# 		)


	# def test_product_table_search(self): 
	# 	self.webdriver.get(self.local_host + "/food/prod_table/")
	# 	self.webdriver.find_element_by_css_selector("input").send_keys(self.test_name_ingredient)
	# 	time.sleep(1)
	# 	self.webdriver.find_element_by_css_selector("input").send_keys(Keys.ENTER)
	# 	time.sleep(1)
	# 	self.assertEquals(
	# 			self.webdriver.find_element_by_id("fat").text,
	# 			"2.0"
	# 		)
	# 	self.assertEquals(
	# 			self.webdriver.find_element_by_id("product_name").text,
	# 			self.test_name
	# 		)
	# 	self.assertEquals(
	# 			self.webdriver.current_url,
	# 			"http://127.0.0.1:8000" +\
	# 			reverse("food:search_results") +\
	# 			"?word=" +\
	# 			self.test_name.replace(" ", "+")
	# 		)


	# @test_log_in_user
	# def test_ingredient_creation(self):
	# 	time.sleep(1)
	# 	self.webdriver.find_element_by_link_text("Ingredients").click()
	# 	self.webdriver.find_element_by_id("ingredient_creation").click()
	# 	ingredinet_name = self.webdriver.find_element_by_id("id_name")
	# 	ingredinet_protein = self.webdriver.find_element_by_id("id_protein")
	# 	ingredinet_carbohydrates = self.webdriver.find_element_by_id("id_carbohydrates")
	# 	ingredinet_fat = self.webdriver.find_element_by_id("id_fat")
	# 	ingredinet_weight = self.webdriver.find_element_by_id("id_quantity_per_portion")
	# 	ingredinet_price = self.webdriver.find_element_by_id("id_price")
	# 	food_type = self.webdriver.find_element_by_xpath("//*[@id='id_food_type']/option[2]")
	# 	add_button = self.webdriver.find_element_by_xpath("/html/body/div/div/form/div/button")

	# 	ingredinet_name.send_keys(self.test_new_name_ingredient)		
	# 	ingredinet_protein.send_keys(10)		
	# 	ingredinet_carbohydrates.send_keys(20)		
	# 	ingredinet_fat.send_keys(30)		
	# 	ingredinet_weight.send_keys(99)		
	# 	ingredinet_price.send_keys("1.99")		
	# 	food_type.click()
	# 	add_button.click()

	# 	self.webdriver.get(
	# 			self.local_host +\
	# 			reverse("food:ingredinet_detail", kwargs={"slug":self.test_new_name})
	# 		)
	# 	delete_button = self.webdriver.find_element_by_xpath("/html/body/div/button[2]/a")
	# 	delete_button.click()
	# 	time.sleep(1)
	# 	delete_confirmation_button = self.webdriver.find_element_by_xpath("/html/body/div/div/form/div/button[1]")
	# 	delete_confirmation_button.click()


	# @test_log_in_user
	# def test_ingredient_creation_validators(self):
	# 	time.sleep(1)
	# 	self.webdriver.find_element_by_link_text("Ingredients").click()
	# 	self.webdriver.find_element_by_id("ingredient_creation").click()
	# 	ingredinet_name = self.webdriver.find_element_by_id("id_name")
	# 	ingredinet_protein = self.webdriver.find_element_by_id("id_protein")
	# 	ingredinet_carbohydrates = self.webdriver.find_element_by_id("id_carbohydrates")
	# 	ingredinet_fat = self.webdriver.find_element_by_id("id_fat")
	# 	ingredinet_weight = self.webdriver.find_element_by_id("id_quantity_per_portion")
	# 	ingredinet_price = self.webdriver.find_element_by_id("id_price")
	# 	food_type = self.webdriver.find_element_by_xpath("//*[@id='id_food_type']/option[2]")
	# 	add_button = self.webdriver.find_element_by_xpath("/html/body/div/div/form/div/button")

	# 	ingredinet_name.send_keys(self.test_name)		
	# 	ingredinet_protein.send_keys(101)		
	# 	ingredinet_carbohydrates.send_keys(1001)		
	# 	ingredinet_fat.send_keys(105)		
	# 	ingredinet_weight.send_keys(587)		
	# 	ingredinet_price.send_keys("999")		
	# 	food_type.click()
	# 	add_button.click()

	# 	name_error = self.webdriver.find_element_by_xpath("//*[@id='error_1_id_name']/strong")
	# 	protein_error = self.webdriver.find_element_by_xpath("//*[@id='error_1_id_protein']/strong")
	# 	carbohydrate_error = self.webdriver.find_element_by_xpath("//*[@id='error_1_id_carbohydrates']/strong")
	# 	fat_error = self.webdriver.find_element_by_xpath("//*[@id='error_1_id_fat']/strong")
	# 	weight_error = self.webdriver.find_element_by_xpath("//*[@id='error_1_id_quantity_per_portion']/strong")
	# 	price_error = self.webdriver.find_element_by_xpath("//*[@id='error_1_id_price']/strong")


	# 	self.assertEquals(
	# 			name_error.text, 
	# 			f"Ingredient {self.test_name.lower()} already exist in db"
	# 		)
	# 	self.assertEquals(
	# 			protein_error.text, 
	# 			f"101.0 > 100 You can't type more than 100g of macroingredients per 100g of product."
	# 		)
	# 	self.assertEquals(
	# 			carbohydrate_error.text, 
	# 			f"1001.0 > 100 You can't type more than 100g of macroingredients per 100g of product."
	# 		)	
	# 	self.assertEquals(
	# 			fat_error.text, 
	# 			f"105.0 > 100 You can't type more than 100g of macroingredients per 100g of product."
	# 		)
	# 	self.assertEquals(
	# 			weight_error.text, 
	# 			f"You cannot enter weight (587), the suggested portion must not exceed 500 grams"
	# 		)	
	# 	self.assertEquals(
	# 			price_error.text, 
	# 			f"Price 999$ is incorrect, you cannot enter a price higher than 199.99$"
	# 		)


	@test_log_in_user
	def test_create_product(self):
		time.sleep(1)
		#Go to menu of creating a new meal
		self.webdriver.find_element_by_link_text("Food").click()
		self.webdriver.find_element_by_link_text("Create new meal").click()

		#Choose the name of the new meal
		product_name = self.webdriver.find_element_by_xpath("//*[@id='id_name']")
		save_product = self.webdriver.find_element_by_xpath("/html/body/div/div/form/div/button")
		product_name.send_keys(self.test_new_name_product)
		save_product.click()
		#Adding some ingredient to meals recipe
		recipe_1 = self.webdriver.find_element_by_xpath("/html/body/div/table[2]/tbody/tr[1]/td[2]/button/a")
		recipe_2 = self.webdriver.find_element_by_xpath("/html/body/div/table[2]/tbody/tr[3]/td[2]/button/a")
		recipe_1.click()
		recipe_2.click()

		
		# self.webdriver.find_element_by_id("ingredient_creation").click()




	# def tearDown(self):
	# 	self.webdriver.close()



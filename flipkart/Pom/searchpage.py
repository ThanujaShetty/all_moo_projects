# Import necessary libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utility.basepage import BasePage


# Create a Page Object for Flipkart Search Page
class FlipkartSearchPage(BasePage):

    def _init_(self, driver):
        self.driver = driver
        self.search_box = (By.XPATH, "//input[@name='q']")
        self.search_button = (By.XPATH, "//button[@type='submit']")

    def search_for_item(self, item):
        search_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.search_box))
        search_input.clear()
        search_input.send_keys(item)
        search_input.submit()




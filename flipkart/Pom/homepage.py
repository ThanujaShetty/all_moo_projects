from selenium.webdriver.common.by import By
from utility.basepage import BasePage

class HomePage(BasePage):
    # Locators
    search_box = (By.NAME, 'q')
    search_button = (By.CLASS_NAME, 'L0Z3Pu')

    def _init_(self, driver):
        super()._init_(driver)
        self.driver.get('https://www.flipkart.com')

    def search_product(self, product_name):
        search_input = self.wait_for_element(self.search_box)
        search_input.send_keys(product_name)
        search_button = self.wait_for_element(self.search_button)
        search_button.click()
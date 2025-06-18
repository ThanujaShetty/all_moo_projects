from selenium.webdriver.common.by import By
from utility.basepage import BasePage


class LoginPage(BasePage):


    def _init_(self, driver):
        super()._init_(driver)
        self.email_input = (By.XPATH, "//input[@class='_2IX_2- VJZDxU']")
        self.password_input = (By.XPATH, "//input[@type='password']")
        self.login_button = (By.XPATH, '//button[text()="Request OTP"]')

    def enter_email(self, email):
        self.driver.find_element(*self.email_input).send_keys(email)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()
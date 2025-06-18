import unittest

import pytest
from selenium import webdriver
from Pom.login import LoginPage

@pytest.mark.usefixtures("setup")
class TestLogin:


    def test_login(self):
        login_page = LoginPage()
        login_page.enter_email("your_email@example.com")
        login_page.click_login()

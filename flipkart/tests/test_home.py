import unittest

import pytest
from selenium import webdriver
from utility.basepage import BasePage

@pytest.mark.usefixtures("setup")
class TestHomePage(BasePage):

    def test_search_product(self,setup):
        self.HomePage.search_product('Laptop')




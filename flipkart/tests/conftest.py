import pytest
from selenium import webdriver
from utility.basepage import BasePage
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="class")
def setup(request):
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    serivce_obj = Service()
    driver = webdriver.Chrome(service=serivce_obj)

    # launching browser
    driver.get("https://www.flipkart.com/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield
    driver.quit()
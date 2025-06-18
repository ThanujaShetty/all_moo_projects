# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
import pytest
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver.get("https://www.tpointtech.com/inheritance-in-python")
# driver.maximize_window()

def multiply(a,b):
    return a * b

@pytest.mark.parametrize("a,b,expected",[(2,3,6),(10,2,20)])
def test_multiply(a,b,expected):
    assert multiply(a,b) == expected


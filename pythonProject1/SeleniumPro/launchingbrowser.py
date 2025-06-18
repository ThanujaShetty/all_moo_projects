from selenium import webdriver
from selenium.webdriver.chrome.service import Service


service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
driver.find_element("name","username").send_keys("Admin")
driver.find_element("name","password").send_keys("admin123")
driver.find_element("css",'button[type="submit"]').click()


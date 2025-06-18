from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach",True)
# serivce_obj = Service()
# driver = webdriver.Chrome()
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#handling alert
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
time.sleep(4)
# driver.find_element(By.ID,"alertbtn").click()
#
# #alert pop-up
# alt = driver.switch_to.alert
# print(alt.text)

#conformation pop-up
# driver.find_element(By.ID,"confirmbtn").click()
# conf_popup= driver.switch_to.alert
# conf_popup.accept()
# conf_popup.dismiss()

alt = driver.switch_to.alert



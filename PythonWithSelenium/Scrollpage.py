from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


import time
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#handling alert
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

# driver.execute_script("window.scrollBy(0,800);")
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
time.sleep(5)
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight);")
time.sleep(5)

ele = driver.find_element(By.XPATH,"//div[contains(text(),Neha)]")
time.sleep(5)
driver.execute_script("arguments[0].scrollIntoView(ele)")
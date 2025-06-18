from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.file.io/")

file_upload = driver.find_element(By.XPATH,'//input[@type="file"][1]')
file_upload.send_keys(r"C:/Users/user/Downloads/Thanuja.pdf")

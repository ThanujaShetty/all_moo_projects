from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up the Chrome WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# Open a website
driver.get("https://www.google.com")

# Maximize the window
driver.maximize_window()

# Wait for 5 seconds
time.sleep(5)

# Close the browser
driver.quit()

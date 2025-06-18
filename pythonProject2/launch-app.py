from flask import Flask
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

app = Flask(__name__)

@app.route('/')
def home():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# launching browser
    driver.get("https://rahulshettyacademy.com/AutomationPractice")
    driver.maximize_window()
    driver.implicitly_wait(10)
    time.sleep(5)

if __name__ == '__main__':
    # Bind to a specific port, e.g., 5000
    app.run(host='0.0.0.0', port=4000)

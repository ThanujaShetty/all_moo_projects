"""# import BY
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver


service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
# driver.find_element("name","username").send_keys("Admin")
# driver.find_element("name","password").send_keys("admin123")
# driver.find_elemen(,'button[type="submit"]').click()"""

import logging
from functools import wraps

# Configure logging
logging.basicConfig(level=logging.INFO)

# Define the decorator
def log_function_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"Calling function: {func.__name__}")
        logging.info(f"Arguments: args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned: {result}")
        return result
    return wrapper

# Example usage
@log_function_call
def add(a, b):
    return a + b

@log_function_call
def greet(name="Guest"):
    return f"Hello, {name}!"

# Call the functions
add(5, 3)
greet(name="Alice")

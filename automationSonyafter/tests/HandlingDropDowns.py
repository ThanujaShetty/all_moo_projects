from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By





# Optional: Automatically manages compatible chromedriver
service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service)

driver.get("https://www.flipkart.com/mobile-phones-store?fm=neo%2Fmerchandising&iid=M_0ad44546-3c85-48a7-99c8-eb6373550e50_1_372UD5BXDFYS_MC.ZRQ4DKH28K8J&otracker=hp_rich_navigation_2_1.navigationCard.RICH_NAVIGATION_Mobiles_ZRQ4DKH28K8J&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_2_L0_view-all&cid=ZRQ4DKH28K8J")
driver.maximize_window()

#click on mobile
driver.find_element(By.XPATH,"//span[contains(text(),'Mobiles')]").click()

listbox = driver.find_element(By.CLASS_NAME,"Gn+jFg")

#scroll till element visible


#select range of mobile
# listbox = driver.find_element(By.CLASS_NAME,"Gn+jFg")
# action.scroll_to_element(listbox).perform()
select = Select(listbox)
select.select_by_visible_text("₹30000")
op=select.o
print(op)

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# Set implicit wait time
driver.implicitly_wait(10)

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

action = ActionChains(driver)
input_field = driver.find_element(By.ID, "input-box")
action.click(input_field)
action.key_down(Keys.SHIFT).send_keys('a').key_up(Keys.SHIFT).perform()





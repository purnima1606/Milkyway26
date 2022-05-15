# CONTEXT_CLICK..................

from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = Chrome(r"C:\Users\user\Desktop\training\chromedriver")
driver.get("http://demowebshop.tricentis.com/")
driver.maximize_window()
sleep(5)

register_link = driver.find_element_by_xpath("//a[text()='Register']")
actions = ActionChains(driver)

# 1
actions.send_keys(register_link).perform()

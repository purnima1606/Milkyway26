from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = Chrome(r"C:\Users\user\Desktop\training\chromedriver")
driver.get("https:\\www.myntra.com")
driver.maximize_window()
sleep(2)

action = ActionChains(driver)

# action.send_keys(Keys.ENTER).perform()
for _ in range(8):
    action.send_keys(Keys.PAGE_DOWN).perform()

sleep(2)

for _ in range(16):
    action.send_keys(Keys.PAGE_UP).perform()


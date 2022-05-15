# SEND_KEYS..................

from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = Chrome(r"C:\Users\user\Desktop\training\chromedriver")
driver.get("http://demowebshop.tricentis.com/")
driver.maximize_window()
sleep(5)

actions = ActionChains(driver)

# 1
actions.send_keys(Keys.PAGE_DOWN).perform()

# 2
actions.send_keys(Keys.PAGE_UP).perform()

# 3
actions.send_keys(Keys.ARROW_DOWN).perform()

# 4
actions.send_keys(Keys.ARROW_UP).perform()

# 5
actions.send_keys(Keys.TAB).perform()

# 6
actions.send_keys(Keys.ENTER).perform()

# 7
actions.send_keys(Keys.ESCAPE).perform()







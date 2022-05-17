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
sleep(1)
# 1
actions.send_keys(Keys.PAGE_DOWN).perform()
sleep(1)

# 2
actions.send_keys(Keys.PAGE_UP).perform()
sleep(1)

# 3
actions.send_keys(Keys.ARROW_DOWN).perform()
sleep(1)

# 4
actions.send_keys(Keys.ARROW_UP).perform()
sleep(1)

# 5
actions.send_keys(Keys.TAB).perform()
sleep(1)

# 6
actions.send_keys(Keys.ENTER).perform()
sleep(1)

# 7
actions.send_keys(Keys.ESCAPE).perform()
sleep(1)






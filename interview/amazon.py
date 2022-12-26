from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = Chrome(r"C:\Users\user\Desktop\training\chromedriver")
driver.get("https:\\www.amazon.com")
driver.maximize_window()
sleep(2)

# search_item = "mobile"
#
# driver.find_element("id", "twotabsearchtextbox").send_keys(search_item)
# sleep(2)
#
# driver.find_element("id", "nav-search-submit-button").click()
# sleep(2)

action = ActionChains(driver)

# sign_in = driver.find_element("id", "nav-link-accountList-nav-line-1")
# action.move_to_element(sign_in).perform()
# sleep(2)
#
# driver.find_element("xpath", "//span[text()='Sign in']").click()
# sleep(2)

# driver.find_element("id", "createAccountSubmit").click()
# sleep(2)

# .....Create a account...........

# name = "purnima singh"
# mobile_no = 9102125597
# password ="chulbul26"
#
# driver.find_element("id", "ap_customer_name").send_keys(name)
# sleep(1)
#
# driver.find_element("id", "ap_email").send_keys(mobile_no)
# sleep(2)
#
# driver.find_element("id", "ap_password").send_keys(password)
# sleep(1)
#
# driver.find_element("name", "passwordCheck").send_keys(password)
# sleep(1)
#
#
# driver.find_element("id", "auth-continue-announce").click()
# sleep(2)

# ......sign in ............

# number = 9102125597
# driver.find_element("id", "ap_email").send_keys(number)
# sleep(2)
#
# driver.find_element("xpath", "//input[@class='a-button-input']").click()
# sleep(2)
#
# driver.find_element("id", "auth-fpp-link-bottom").click()
# sleep(2)
#
# driver.find_element("xpath", "//input[@class='a-button-input']").click()
# sleep(2)
#
# input("enter any key")
# sleep(5)
#
# driver.maximize_window()
# sleep(3)
# # ??????????????????????????????????????
# # action.move_to_element("xpath", "//span[text()='Continue']").perform()
# # sleep(2)
#
# driver.find_element("xpath", "//input[@class='a-button-input notranslate']").click()
# sleep(2)
#

#...................

# action.send_keys(Keys.PAGE_DOWN).perform()
# sleep(7)

# action.send_keys(Keys.PAGE_UP).perform()
# sleep(7)
#
# action.send_keys(Keys.ARROW_DOWN).perform()
# sleep(4)
#
# action.send_keys(Keys.ARROW_UP).perform()
# sleep(4)

# action.send_keys(Keys.TAB).perform()
# sleep(2)
#
# action.send_keys(Keys.ENTER).perform()
# sleep(2)
#
# action.send_keys(Keys.ESCAPE).perform()
# sleep(2)

# ......

new_release =driver.find_elements("xpath", "//a[text()='New Releases']")
print(new_release)      # []

for item in new_release:
    print(item.text)
    sleep(2)

# driver.find_element()
# //span[@class='a-button-text']

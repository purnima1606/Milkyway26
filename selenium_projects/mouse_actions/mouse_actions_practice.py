# # ............. MOVE_TO_ELEMENT ..................
#
# from selenium.webdriver import Chrome
# from time import sleep
# from selenium.webdriver.common.action_chains import ActionChains
#
# driver = Chrome(r"C:\Users\user\Desktop\training\chromedriver")
# driver.get("https://www.myntra.com")
# driver.maximize_window()
# sleep(5)
#
# actions = ActionChains(driver)
#
# profile = driver.find_element_by_xpath("//span[text()='Profile']")
#
# # mouse over on profile...
# actions.move_to_element(profile).perform()
# sleep(2)
#
#
# driver.find_element_by_xpath("//a[text()='login / Signup']").click()
# sleep(1)
#
# driver.find_element_by_xpath("//input[@class='form-control mobileNumberInput']").send_keys("9102125597")
# sleep(1)
#
# # //div[text()='CONTINUE']
# driver.find_element("xpath", "//div[text()='CONTINUE']").click()
# sleep(32)
#
# driver.find_element("xpath", "//div[text()='CONTINUE']").click()
# sleep(2)

#####################################################################################################################
#
# # MOVE_TO_ELEMENT..................
#
# from selenium.webdriver import Chrome
# from time import sleep
# from selenium.webdriver.common.action_chains import ActionChains
#
# driver = Chrome(r"C:\Users\user\Desktop\training\chromedriver")
# driver.get("https://www.monsterindia.com")
# driver.maximize_window()
# sleep(2)
#
# actions = ActionChains(driver)
#
# jobs_search = driver.find_element_by_xpath("//a[text()='Job search']")
#
# actions.move_to_element(jobs_search).perform()
# sleep(1)
#
# jobs_by_skills = driver.find_element_by_xpath("//a[text()='Jobs by Skills']")
#
# actions.move_to_element(jobs_by_skills).perform()
# sleep(1)
#
# python_jobs = driver.find_element_by_xpath("//a[contains(text(),'Python Jobs')]")
# actions.move_to_element(python_jobs).perform()
# sleep(1)
#
# python_jobs.click()        # SE_home_autocomplete
#
# skill = driver.find_element_by_id("SE_home_autocomplete").send_keys("python")
# actions.move_to_element(skill).perform()
# sleep(1)
#
# #SE_home_autocomplete
# # location = driver.find_element_by_xpath("//input[@class='input location_ac']").send_keys("banglore")
# # location = driver.find_element_by_id("SE_home_autocomplete").send_keys("banglore")
# location = driver.find_element("name", "lmy").send_keys("banglore")
# actions.move_to_element(location).perform()
# sleep(1)
#

################################################################################################
# ................. DUBLE CLICK .........................

# from selenium.webdriver import Chrome
# from time import sleep
# from selenium.webdriver.common.action_chains import ActionChains
#
# driver = Chrome(r"C:\Users\user\Desktop\training\chromedriver")
# driver.get("file:///C:/Users/user/Desktop/google_drive%20folder/demo.html")
# driver.maximize_window()
# sleep(5)
#
# actions = ActionChains(driver)
#
# click_me = driver.find_element_by_xpath("//button[text()='Double-click me']")
#
# actions.double_click(click_me).perform()
#
# # # .........................execute properly.........................
#
#
#
#################################################################################################
#
# # SEND_KEYS..................
#
# from selenium.webdriver import Chrome
# from time import sleep
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
#
# driver = Chrome(r"C:\Users\user\Desktop\training\chromedriver")
# driver.get("http://demowebshop.tricentis.com/")
# driver.maximize_window()
# sleep(5)
#
# actions = ActionChains(driver)
# sleep(1)
# # 1
# for _ in range(2):
#     actions.send_keys(Keys.PAGE_DOWN).perform()
#     sleep(1)

# actions.send_keys(Keys.PAGE_DOWN).perform()
# sleep(1)

# # 2
# actions.send_keys(Keys.PAGE_UP).perform()
# sleep(1)
#
# # 3
# actions.send_keys(Keys.ARROW_DOWN).perform()
# sleep(1)
#
# # 4
# actions.send_keys(Keys.ARROW_UP).perform()
# sleep(1)
#
# # 5
# actions.send_keys(Keys.TAB).perform()
# sleep(1)
#
# # 6
# actions.send_keys(Keys.ENTER).perform()
# sleep(1)
#
# # 7
# actions.send_keys(Keys.ESCAPE).perform()
# sleep(1)
#

############################################################################################
# .................... HOTSTAR ............................

from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = Chrome(r"C:\Users\user\Desktop\training\chromedriver")
driver.get("http://hotstar.com/")
driver.maximize_window()
sleep(5)

actions = ActionChains(driver)
sleep(1)

for _ in range(10):
    actions.send_keys(Keys.PAGE_DOWN).perform()
    sleep(1)

# driver.find_element("xpath", "//p[text()='Connect with us']")
# //p[text()='Connect with us']

# actions.send_keys(Keys.PAGE_DOWN).perform()
# sleep(1)
#






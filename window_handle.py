from selenium.webdriver import Chrome
from time import sleep
import re
# /session/{session id}/window/maximize
driver = Chrome(r"C:\Users\user\Desktop\training\chromedriver")
#sleep(3)

# /session/{session id}/url --> POST
driver.get("file:///C:/Users/user/Desktop/google_drive%20folder/demo.html")
sleep(3)

driver.find_element_by_id("delete").click()
sleep(2)

driver.switch_to_alert.accept()

driver.find_element_id("delete").click()
sleep(2)

driver.switch_to_alert.dismiss()
sleep(2)

driver.find_element_id("delete").click()
sleep(2)


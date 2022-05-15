from selenium.webdriver import Chrome
from time import sleep

driver = Chrome(r"C:\Users\user\Desktop\training\chromedriver")

driver.get("http://demowebshop.tricentis.com/")
sleep(2)

driver.find_element_by_class("ico-register").click()
sleep(2)


driver.find_element_by_css_selector("input[value='M']").click()
sleep(1)

driver.find_element_by_id("FirstName").send_keys("hello")
sleep(2)

driver.find_element_by_id("LastName").send_keys("world")
sleep(1)

#driver.close()




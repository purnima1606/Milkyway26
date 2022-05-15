from selenium.webdriver import Chrome
from time import sleep

driver = Chrome(r"C:\Users\user\Desktop\training\chromedriver")

driver.get("http://demowebshop.tricentis.com/")
sleep(2)

driver.find_element_by_class_name("ico-register").click()
sleep(2)


driver.find_element_by_id("gender-male").click()
sleep(1)

driver.find_element_by_name("FirstName").send_keys("hello")
sleep(2)

driver.find_element_by_name("LastName").send_keys("world")
sleep(1)

driver.find_element_by_name("Email").send_keys("hello.world@company.com")
sleep(1)

driver.find_element_by_name("Password").send_keys("Password123")
sleep(2)

driver.find_element_by_name("ConfirmPassword").send_keys("Password123")
sleep(4)

driver.find_element_by_name("register-button").click()
                                        
#driver.close()




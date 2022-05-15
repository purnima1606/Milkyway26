from selenium.webdriver import Chrome
from time import sleep

driver = Chrome(r"C:\Users\user\Desktop\training\chromedriver")

driver.get("http://demowebshop.tricentis.com/")
sleep(2)

#driver.find_element_by_css_selector("a[class='ico-register']").click()
driver.find_element_by_class_name("ico-register").click()
sleep(2)

# radio button, Firstname, Lastname, Email, Password, ConfirmPassword, resister_button

#driver.find_element_by_css_selector("input[value='M']").click()
#driver.find_element_by_name("Gender").click   ## this is not posible
driver.find_element_by_id("gender-male").click() 
sleep(1)

#driver.find_element_by_css_selector("input[name='FirstName']").send_keys("hello")
#driver.find_element_by_id("FirstName").send_keys("hello")
driver.find_element_by_name("FirstName").send_keys("hello")

sleep(2)

#driver.find_element_by_css_selector("input[name='LastName']").send_keys("world")
#driver.find_element_by_id("LastName").send_keys("world")
driver.find_element_by_name("LastName").send_keys("world")
sleep(1)


#driver.find_element_by_css_selector("input[name='Email']").send_keys("hello.world@company.com")
#driver.find_element_by_id("Email").send_keys("hello.world@company.com")
driver.find_element_by_name("Email").send_keys("hello.world@company.com")
sleep(3)

#driver.find_element_by_css_selector("input[name='Password']").send_keys("Password123")
#driver.find_element_by_id("Password").send_keys("Password123")
driver.find_element_by_name("Password").send_keys("Password123")
sleep(2)

#driver.find_element_by_css_selector("input[name='ConfirmPassword']").send_keys("Password123")
#driver.find_element_by_id("ConfirmPassword").send_keys("Password123")
driver.find_element_by_name("ConfirmPassword").send_keys("Password123")
sleep(4)


#driver.find_element_by_css_selector("input[name='register-button']").click()
#driver.find_element_by_id("register-button").click()
driver.find_element_by_name("register-button").click()

                                        
#driver.close()

from selenium.webdriver import Chrome
from time import sleep

driver = Chrome(r"C:\Users\user\Desktop\training\chromedriver")

driver.get("http://demowebshop.tricentis.com/")
sleep(2)

driver.find_element_by_css_selector("a[class='ico-register']").click()
sleep(1)


driver.find_element_by_css_selector("input[value='M']").click()
sleep(1)

driver.find_element_by_css_selector("input[name='FirstName']").send_keys("hello")
sleep(2)

driver.find_element_by_css_selector("input[name='LastName']").send_keys("world")
sleep(1)

driver.find_element_by_css_selector("input[name='Email']").send_keys("hello.world@company.com")
sleep(2)

driver.find_element_by_css_selector("input[name='Password']").send_keys("Password123")
sleep(1)

driver.find_element_by_css_selector("input[name='ConfirmPassword']").send_keys("Password123")
sleep(1)

driver.find_element_by_css_selector("input[name='register-button']").click()
sleep(1)

#driver.close()




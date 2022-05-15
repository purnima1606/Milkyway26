from selenium.webdriver import Chrome
from time import sleep

driver = Chrome(r"C:\Users\user\Desktop\training\chromedriver")

driver.get("http://demowebshop.tricentis.com/")
sleep(2)

#driver.find_element_by_css_selector("a[class='ico-register']").click()
#driver.find_element_by_class_name("ico-register").click()
p_register = driver.find_element_by_partial_link_text(("Inbox").click()
link_register = driver.find_element_by_link_text("Register")
link_register.click()
sleep(3)

print(type(link_register))
print(link_register)
print(p_register)

rdo_male = driver.find_element_by_id("gender-male")
rdo_male.click()
sleep(1)

#txt_fname = driver.find_element_by_name("FirstName")
txt_fname = driver.find_element_by_id("FirstName")
txt_fname.send_keys("hello")
sleep(2)

#txt_lname = driver.find_element_by_name("LastName")
txt_lname = driver.find_element_by_id("LastName")
txt_lname.send_keys("world")
sleep(1)

#txt_email = driver.find_element_by_name("Email")
txt_email = driver.find_element_by_id("Email")
txt_email.send_keys("hello.world@company.com")
sleep(1)

#txt_password = driver.find_element_by_name("Password")
txt_password = driver.find_element_by_id("Password")
txt_password.send_keys("Password123")
sleep(2)


#txt_confirm_password = driver.find_element_by_name("ConfirmPassword")
txt_confirm_password = driver.find_element_by_id("ConfirmPassword")
txt_confirm_password.send_keys("Password123")
sleep(4)

#btn_register = driver.find_element_by_name("register-button")
btn_register = driver.find_element_by_id("register-button")
btn_register.click()




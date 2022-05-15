from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.support.select import Select


# /session/{session id}/window/maximize
driver = Chrome(r"C:\Users\user\Desktop\training\chromedriver")
sleep(3)

driver.get("C:/Users/user/Desktop/google_drive%20folder/demo.html")
sleep(3)
"""
#WebElement Method
#1.click()
#2.send.keys()
#3.text(property)
#4.get_attribute()

#Dependent and Independent elements
#2.write the xpath of Independent element and move up the html tree till such point where both dependent
#and independent are getting covered under one common node or parent
#3.write the xpath of dependent element

driver.find_element_by_xpath("//td[text()='Python']/..//input[@name='download']").click()
sleep(2)
driver.find_element_by_xpath("//td[text()='Java']/..//input[@name='download']").click()
sleep(2)
driver.find_element_by_xpath("//td[text()='C#']/..//input[@name='download']").click()
sleep(3)
driver.find_element_by_xpath("//td[text()='Perl']/..//input[@name='download']").click()
sleep(3)
"""

"""
element = driver.find_element_by_id("multiple_cars")

def select_all():
    s= Select(element)
    items = s.options

# list comprehension
data = [item.text for item in items]

for item in data:
    s.select_by_visible_text(item)
    sleep(3)
"""


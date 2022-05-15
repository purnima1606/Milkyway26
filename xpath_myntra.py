from selenium.webdriver import Chrome
from time import sleep
import re
# /session/{session id}/window/maximize
driver = Chrome(r"C:\Users\user\Desktop\training\chromedriver")
#sleep(3)

# /session/{session id}/url --> POST
driver.get("https://www.myntra.com/kids?f=Categories%3aTshirts%3A%3AGender%3Aboys%2Cboys%20girls")
sleep(10)


element_discount = driver.find_elements_by_xpath("//span[@class='product-discountPercentage']") 

element_tshirts = driver.find_elements_by_xpath("//span[@class='product-discountPercentage']/../..//h4[@class='product-product']")

#
discount = [item.text for item in element_discount]

#
tshirt_names = [item.text for item in element_tshirts]

actual_discount = []

for name, item in zip(tshirt_names, discount):
   actual_discount.append((name, item))
   

print(actual_discount)   

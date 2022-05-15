from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.support.select import Select
import csv

# /session/{session id}/window/maximize
driver = Chrome(r"C:\Users\user\Desktop\training\chromedriver")
sleep(3)
"""
driver.get("C:/Users/user/Desktop/google_drive%20folder/demo.html")
sleep(3)

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
driver.get("http://www.python.org/downloads/")
sleep(6)

driver.find_element_by_xpath("//a[text()='Python 3.9.10']/../..//a[text()='Release Notes']").click()

#driver.find_element_by_xpath("//a[text()='Python 3.9.10']/../..//a[text()='Release Notes']").click()
sleep(2)
"""

"""

def read_csv():
    with open("c:/User/user/Desktop/training/price.csv") as file:
        rows = csv.reader(file)
        headers = next(rows)
        expected_prices = {row[0]:float(row[1]) for row in rows}
    return  expected_prices

 expected_prices = read_csv()

 for product, expected_price in expected_prices.items():
     sleep(3)
     actual_price = driver.find_element_by_xpat(f"//a[text()='{product}']/../..//span[@class='price']")
     if expected_price == float(actual_price):
         print("PASS")
     else:
         print(f"The expected price of {product} is {expected_price} but the actual displayed is {actual_price}")
                                                
"""    













            

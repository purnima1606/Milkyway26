from selenium.webdriver import Chrome
from time import sleep
import re
# /session/{session id}/window/maximize
driver = Chrome(r"C:\Users\user\Desktop\training\chromedriver")
#sleep(3)

# /session/{session id}/url --> POST
driver.get("http://services.smartbear.com/samples/TestComplete14/smartstore/newproducts")
sleep(5)

# Get all products (webelement)
element_items = driver.find_elements_by_xpath("//h3[@class='art-name']/a/span")

# Get all prices(webelement)
element_prices = driver.find_elements_by_xpath("//span[@class='art-price'or @class='art-price art-price']")

"""
for item in element_items:
    print(item.text)
    sleep(0.5)


for item in element_prices:
    print(item.text)
    sleep(0.5)
    
"""

all_items = [item.text for item in element_items]

all_prices = []

for item in element_prices:
    actual_price = item.text
    actual_price = float("".join(re.findall(r"[\d\.]", actual_price)))
    all_prices.append(actual_price)


print(all_prices)
print("*"*60)


actual_prices = {}
for product, price in zip(all_items, all_prices):
    actual_prices[product] = price
    
    
print(actual_prices)
print("*"*60)


# products with less than $100
less_100 = {product:price for product, price in actual_price.items() if price < 100 }
print(less_100)








                                               

from selenium.webdriver import Chrome
from time import sleep

# /session/{session id}/window/maximize
driver = Chrome(r"C:\Users\user\Desktop\training\chromedriver")
sleep(3)

# /session/{session id}/url --> POST
driver.get("file:///C:/Users/user/Desktop/google_drive%20folder/demo.html")
sleep(8)

items = ["AA", "AAPL", "MSFT"]

for item in items:
    print(item, end=" ")

print()

print("-"*40)

while True:
    for item in items:
        price = driver.find_element_by_xpath(f"//td[text()='{item}']/..//td[@class='price']").text
        print(price, end="\t")
    print()
    sleep(2)


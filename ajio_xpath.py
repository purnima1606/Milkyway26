from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.support.select import Select
# /session/{session id}/window/maximize
driver = Chrome(r"C:\Users\user\Desktop\training\chromedriver")
sleep(1)

driver.get("https://ajio.com")
driver.maximize_window()

driver.find_element_by_xpath("//input[@role='combobox']").send_keys("shoes for boys")
sleep(5)
driver.find_element_by_xpath("//span[@class='ic-search']").click()
sleep(5)
b=driver.find_element_by_xpath("//select")
d=Select(b)
d.select_by_visible_text("Price (highest first)")
p=driver.find_elements_by_xpath("//div[@class='contentHolder']")
sleep(4)
c=0
for i in p:
    c += 1
    if c <= 6:
        print(i.text)
        print(":.................")
        

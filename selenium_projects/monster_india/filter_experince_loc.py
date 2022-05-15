from selenium.webdriver import Chrome
from time import sleep

driver = Chrome(r"C:\Users\user\Desktop\training\chromedriver")

driver.get("https://www.monster_india.com/")
driver.find_element_by_xpath("//input[@class='input search-bar home_ac']").send_keys("python")
sleep(2)


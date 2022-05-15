from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

driver = Chrome(r"C:\Users\user\Desktop\training\chromedriver")
driver.get("https://www.goibibo.com")
driver.maximize_window()
sleep(5)

driver.find_element_by_xpath("//span[text()='Departure']").click()
sleep(3)

driver.find_element_by_xpath("//div[text()='September 2022']/../..//p[text()='26']").click()


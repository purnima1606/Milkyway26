
from selenium.webdriver import Chrome
from time import sleep

# /session/{session id}/window/maximize
driver = Chrome(r"C:\Users\user\Desktop\training\chromedriver")
sleep(3)

# /session/{session id}/url --> POST
driver.get("https://www.ajio.com/")
sleep(1)

driver.find_element_by_xpath("//input[@name='searchVal']").send_keys("shoes for boys ")

#driver.find_element_by_xpath(f"//*[@id='appContainer']/div[1]/div/header/div[3]/div[2]/form/div").click()
#driver.find_element_by_xpath(f"//*[@id='facets']/div[2]/ul/li[2]/div/div/div[1]/span[2]")
#driver.find_element_by_xpath("//span[text()='shoes']").click()
driver.find_element_by_xpath()


#for item in items:
#   driver.find_element_by_xpath(f"")
#  sleep(1)

#driver.find_element_by_xpath()

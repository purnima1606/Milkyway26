from selenium.webdriver import Chrome
from time import sleep

driver = Chrome(r"C:\Users\user\Desktop\training\chromedriver")

driver.get("http://demowebshop.tricentis.com/")
driver.maximize_window()
sleep(3)

driver.find_element_by_xpath("//a[text()='Twitter']").click()
sleep(3)

handles = driver.window_handles

driver.switch_to.window(handles[1])
sleep(10)

driver.find_element_by_xpath("//input[@data-testid='SearchBox_Search_Input']").send_keys("hello")
sleep(5)
driver.switch_to.window(handles[0])
sleep(3)

driver.find_element_by_xpath("//a[text()='Register']").click()

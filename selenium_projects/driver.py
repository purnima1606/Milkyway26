from selenium.webdriver import Chrome
from time import sleep

driver = Chrome(r"C:\Users\user\Desktop\training\chromedriver")
#driver = Chrome(r"C:\Users\user\Desktop\training")
sleep(3)

driver.get("http://demowebshop.tricentis.com/")
sleep(3)

driver.maximize_window()
sleep(3)

driver.minimize_window()
sleep(3)

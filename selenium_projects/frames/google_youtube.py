from selenium.webdriver import Chrome
from time import sleep

driver = Chrome(r"C:\Users\user\Desktop\training\chromedriver")
driver.get("https://www.google.com")
driver.maximize_window()
sleep(4)

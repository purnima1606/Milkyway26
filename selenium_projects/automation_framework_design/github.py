from selenium.webdriver import Chrome
from time import sleep

driver = Chrome("./chromedriver")

driver.get("https://github.com/")
sleep(2)
driver.maximize_window()


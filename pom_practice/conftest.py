from selenium.webdriver import Chrome
from time import sleep
from pytest import fixture

@fixture
def setup():
    driver = Chrome(r"C:\Users\user\Desktop\training\chromedriver")
    driver.get("http://demowebshop.tricentis.com/")
    driver.maximize_window()
    sleep(2)
    yield driver
    driver.close()

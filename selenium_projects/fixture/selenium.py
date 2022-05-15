from pytest import fixture
from selenium import WebDriver

@fixture
def _driver():
    driver = WebDriver.Chrome(r"C:\Users\user\Desktop\training\chromedriver")
    driver.get("http://google.com")
    return driver

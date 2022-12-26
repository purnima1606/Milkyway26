from selenium.webdriver import Chrome
from pytest import fixture

@fixture
def _driver():
    driver = Chrome(r"C:\Users\user\Desktop\training\chromedriver")
    # driver.get("http://google.com")
    return driver

from pytest import fixture
from selenium.webdriver import Chrome

@fixture
def greet():
    print("hello world")

###################################
# from pytest import fixture
# from selenium.webdriver import Chrome

@fixture
def _driver():
    driver = Chrome(r"C:\Users\user\Desktop\training\chromedriver")
    driver.get("http://demowebshop.tricentis.com/")
    return driver

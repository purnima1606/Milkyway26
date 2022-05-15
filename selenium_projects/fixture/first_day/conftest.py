from selenium.webdriver import Chrome
from pytest import fixture

@fixture                  # (scope="class")
def setup():
    driver = Chrome(r"C:\Users\user\Desktop\training\chromedriver")
    driver.get("http://demowebshop.tricentis.com/")
    yield driver
    driver.close()

@fixture                         # (scope="class")
def greet():
    print("Executing before class")
    yield "hello world"
    print("Executing After class")



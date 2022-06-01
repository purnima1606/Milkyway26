from selenium.webdriver import Chrome

from pytest import fixture
@fixture
def setup():
    driver = Chrome(r"C:\Users\user\Desktop\training\chromedriver")
    driver.get("http://demowebshop.tricentis.com/")
    yield driver
    driver.close()



# setup and tail down

# from pytest import fixture
#
# @fixture
# def greet():
#     print("hello world")
#
#
# # passing fixture to test method
# def test_greet(greet):     # passing fixture as an argument to test function
#     return "hello world" == greet


# from pytest import fixture
# from selenium.webdriver import Chrome
#
# @fixture
# def _driver():
#     driver = Chrome(r"C:\Users\user\Desktop\training\chromedriver")
#     driver.get("http://demowebshop.tricentis.com/")
#     return driver
#
##############################################
#
#
# def test_login(_driver):     # passing fixture as an argument to test function
#     _driver.find_element_by_xpath("//a[text()='Log in']").click()
#     _driver.find_element_by_id("Email").send_keys("steve.job@company.com")
#     _driver.find_element_by_id("Password").send.keys("password123")
#     _driver.quit()

#############################################


# from pytest import fixture
from selenium.webdriver import Chrome


# @fixture
def _driver():
    print("launching browser")
    driver = Chrome(r"C:\Users\user\Desktop\training\chromedriver")
    print(driver)
    driver.get(r"http://demowebshop.tricentis.com/")
    return driver
    # yield driver       # passing driver instance to test method
    # print("closing browser")
    # driver.quit()


def test_login(_driver):     # passing fixture as an argument to test function
    _driver.find_element_by_xpath("//a[text()='Log in']").click()
    _driver.find_element_by_id("Email").send_keys("hello.world@company.com")
    _driver.find_element_by_id("Password").send.keys("password123")
    _driver.quit()









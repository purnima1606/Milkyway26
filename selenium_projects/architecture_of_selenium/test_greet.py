from time import sleep

# greet is present in conftest.py file

def test_greet(greet):     # passing fixture as an argument to test function
    return "hello world" == greet

# execute
# test_greet.py::test_greet hello world
# PASSED                                         [100%]


def test_login(_driver):     # passing fixture as an argument to test function
    _driver.find_element_by_xpath("//a[text()='Log in']").click()
    _driver.find_element_by_id("Email").send_keys("steve.job@company.com")
    sleep(4)
    _driver.find_element_by_id("Password").send.keys("password123")
    sleep(4)

    _driver.quit()

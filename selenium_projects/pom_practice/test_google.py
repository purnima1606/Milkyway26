from time import sleep

def test_google(_driver):
    _driver.get("http://google.com")
    _driver.maximize_window()
    sleep(1)
t
#
# def test_myntra(_driver):
#     _driver.get("http://myntra.com")
#     _driver.maximize_window()
#     sleep(1)
#
#
# def test_hotstar(_driver):
#     _driver.get("http://google.com")
#     _driver.maximize_window()
#     sleep(1)

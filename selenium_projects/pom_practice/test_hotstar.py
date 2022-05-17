from time import sleep

def test_hotstar(_driver):
    _driver.get("http://hotstar.com")
    _driver.maximize_window()
    sleep(1)

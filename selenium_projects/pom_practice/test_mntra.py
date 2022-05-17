from time import sleep

def test_myntra(_driver):
    _driver.get("http://myntra.com")
    _driver.maximize_window()
    sleep(1)

from time import sleep


class Test_001_google:
    def test_google(self,_driver):
        self._driver = _driver
        self._driver.get("http://google.com")
        self._driver.maximize_window()
        sleep(10)


    def test_myntra(self,_driver):
        self._driver = _driver
        self._driver.get("http://myntra.com")
        self._driver.maximize_window()
        sleep(10)


    def test_hotstar(self,_driver):
        self._driver = _driver
        self._driver.get("http://google.com")
        self._driver.maximize_window()
        sleep(10)

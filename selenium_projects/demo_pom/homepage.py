from seleniumWrapper import SeleniumWrapper
from selenium.webdriver import Chrome
class Homepage(SeleniumWrapper):
    _clk_register = ("link text", "Register")
    _clk_login = ("link text", "Log in")

    def __init__(self, driver):
        self.driver = driver
    def home_click_login(self):
        self.click_element(self._clk_login)
    def home_click_register(self):
        self.click_element(self._clk_register)



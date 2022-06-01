from selenium.webdriver import Chrome
from wait import wait
from time import sleep
class SeleniumWrapper:
    def __init__(self, driver):
        self.driver = driver

    @wait   # enter_text = wait(enter_text)
    def enter_text(self, locator, *, value):
        self.driver.find_element(*locator).send_keys(value)

    @wait   # click_element = wait(click_element)
    def click_element(self, locator):
        self.driver.find_element(*locator).click()


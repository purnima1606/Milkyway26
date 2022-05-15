from demo import _wait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Chrome


from selenium.webdriver.support.select import Select
# import csv
# import re


class SeleniumWrapper:
    def __init__(self):
        self.driver = Chrome(r"C:\Users\user\Desktop\training\chromedriver")

    @_wait   # enter_text = wait(enter_text)
    def enter_text(self, locator, *, value):
        self.driver.find_element(*locator).send_keys(value)

    @_wait   # click_element = wait(click_element)
    def click_element(self, locator):
        self.driver.find_element(*locator).click()

    @_wait       # select_item = wait(select_item)
    def select_item(self, locator, *, item):
        element = self.driver.find_element(*locator)
        s = Select(element)
        if isinstance(item, str):
            s.select_by_visible_text(item)
        elif isinstance(item, int):
            s.select_by_index(item)
        else:
            raise TypeError(f"Invalid Type {item}")

    @_wait
    def select_items(self, locator, *, items):
        for _item in items:
            try:
                self.select_item(locator, item=_item)
            except NoSuchElementException:
                print(f"Could not find item {_item}")
                continue





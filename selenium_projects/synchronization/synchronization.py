from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Chrome
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.select import Select
driver = Chrome(r"C:\Users\user\Desktop\training\chromedriver")
# driver.get(demo.html)
driver.get(r"http://demowebshop.tricentis.com/")




class _visibility_of_element_located(visibility_of_element_located):
    def __init__(self, locator):
        super().__init__(locator)

    def __call__(self, driver):
        result = super().__call__(driver)
        if isinstance(result, WebElement):
            return  result.is_enabled()
        return result


def wait(func):
    def wrapper(*args, **kwargs):
        instance = args[0]
        locator = args[1]
        wait = WebDriverWait(instance.driver, 10)
        v = _visibility_of_element_located(locator)
        wait.until(v)
        return func(*args, **kwargs)
    return wrapper

class SeleniumWrapper:
    def __init__(self, driver):
        self.driver = driver

    @wait
    def enter_text(self, locator, * ,value):
        self.driver.find_element(*locator).send_keys(value)

    @wait
    def click_element(self, locator):
        self.driver.find_element(*locator).click()

    @wait
    def select_item(self, locator, *, item):
        element = self.driver.find_element(*locator)
        s = Select(element)
        if isinstance(item, str):
            s.select_by_visible_text(item)
        elif isinstance(item, int):
            s.select_by_index(item)
        else:
            raise TypeError(f"Invalid type{item}")

    @wait
    def select_items(self, locator, *, items):
        for _item in items:
            try:
                self.select_item(locator, item=_item)
            except NoSuchElementException:
                print(f"could not find item {_item}")

s1 =SeleniumWrapper()
# s1.click_element(('link text', 'Register'))
s1.enter_text(("id", "FirstName"), value ="hello")
# s1.select_items(("id", "multiple_cars"), items=['Mercedes', 'Audi', 'Mini', 'BMW'])
# s1.select_item(("id", "standard_cars"), item="Audi")














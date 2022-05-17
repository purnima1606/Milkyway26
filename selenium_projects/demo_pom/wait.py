from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait

class _visibility_of_element_located(visibility_of_element_located):
    def __init__(self, locator):
        super().__init__(locator)

    def __call__(self, driver):
        result = super().__call__(driver)
        # Checking if __call__ has returned a WebElement?
        if isinstance(result, WebElement):
            return result.is_enabled()
        return result

def wait(func):
    def wrapper(*args, **kwargs):       # args = (self, ("id", "multiple_cars"))
        instance = args[0]
        locator = args[1]       # get the inner tuple
        # Wait (3 Conditions)
        wait = WebDriverWait(instance.driver, 10)
        v = _visibility_of_element_located(locator)
        wait.until(v)
        return func(*args, **kwargs)        # original func is executed (click_element, enter_text)
    return wrapper

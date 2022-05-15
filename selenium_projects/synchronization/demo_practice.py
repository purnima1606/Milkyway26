#
# # from selenium.webdriver import Chrome
# # from time import sleep
# # from selenium.webdriver.support.select import Select
# # import csv
# # import re
# # from selenium.common.exceptions import NoSuchElementException
# # from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.support.expected_conditions import visibility_of_element_located
# # from selenium.webdriver.remote.webelement import WebElement
# # from selenium.webdriver.common.action_chains import ActionChains
# #
# # driver = Chrome(r"C:\Users\user\Desktop\training\chromedriver")
# # driver.get("file:///C:/Users/user/Desktop/google_drive%20folder/loading.html")
# # sleep(5)
# #
# # class _visibility_of_element_located(visibility_of_element_located):
# #     def __init__(self, locator):
# #         super().__init__(locator)
# #
# #     def __call__(self, driver):
# #         result = super().__call__(driver)
# #         # Checking if __call__ has returned a WebElement?
# #         if isinstance(result, WebElement):
# #             return result.is_enabled()
# #         return result
# #
# #
# #
# # wait = WebDriverWait(driver,10)
# # v = _visibility_of_element_located(("name", "fname"))
# # wait.until(v)
# # print("done")   # done
# #
# # driver.find_element_by_name("fname").send_keys("Hello")
# # execute properly
#
# #########################################################
#
# from selenium.webdriver import Chrome
# from time import sleep
# from selenium.webdriver.support.select import Select
# import csv
# import re
# from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support.expected_conditions import visibility_of_element_located
# from selenium.webdriver.remote.webelement import WebElement
# from selenium.webdriver.common.action_chains import ActionChains
#
#
# class _visibility_of_element_located(visibility_of_element_located):
#     def __init__(self, locator):
#         super().__init__(locator)
#
#     def __call__(self, driver):
#         result = super().__call__(driver)
#         # Checking if __call__ has returned a WebElement?
#         if isinstance(result, WebElement):
#             return result.is_enabled()
#         return result
#
#
# def enter_text( locator, *, value):
#     driver.find_element(*locator).send_keys(value)
#
#
# def click_element(locator):
#     driver.find_element(*locator).click()
#
#
# def select_item():
#     ...
#
# driver = Chrome(r"C:\Users\user\Desktop\training\chromedriver")
# driver.get(r"http://demowebshop.tricentis.com")
# sleep(5)
#
# click_element(("link text", "Register"))
# sleep(2)
#
# click_element(("id", "gender-male"))
# sleep(2)
#
# enter_text(("id", "FirstName"), value="hello")
# sleep(2)
#
# enter_text(("id", "LastName"), value="world")
# sleep(2)
#
# enter_text(("id", "Email"), value="hello.world@company.com")
# sleep(2)
#
# enter_text(("id", "Password"), value="password123")
# sleep(2)
#
# enter_text(("id", "ConfirmPassword"), value="password123")
# sleep(2)
#
# click_element(("id", "register-button"))
# sleep(2)
#
# # execute


##################################################################################

# from selenium.webdriver import Chrome
# from time import sleep
# from selenium.webdriver.support.select import Select
# import csv
# import re
# from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support.expected_conditions import visibility_of_element_located
# from selenium.webdriver.remote.webelement import WebElement
# from selenium.webdriver.common.action_chains import ActionChains
#
#
# class _visibility_of_element_located(visibility_of_element_located):
#     def __init__(self, locator):
#         super().__init__(locator)
#
#     def __call__(self, driver):
#         result = super().__call__(driver)
#         # Checking if __call__ has returned a WebElement?
#         if isinstance(result, WebElement):
#             return result.is_enabled()
#         return result
#
# def wait(func):
#     def wrapper(*args, **kwargs):       # args = (self, ("id", "multiple_cars"))
#         instance = args[0]
#         locator = args[1]       # get the inner tuple
#         # Wait (3 Conditions)
#         wait = WebDriverWait(instance.driver, 10)
#         v = _visibility_of_element_located(locator)
#         wait.until(v)
#         return func(*args, **kwargs)        # original func is executed (click_element, enter_text)
#     return wrapper
#
# class SeleniumWrapper:
#     def __init__(self, driver):
#         self.driver = driver
#
#     @wait   # enter_text = wait(enter_text)
#     def enter_text(self, locator, *, value):
#         self.driver.find_element(*locator).send_keys(value)
#
#     @wait   # click_element = wait(click_element)
#     def click_element(self, locator):
#         self.driver.find_element(*locator).click()
#
#     @wait       # select_item = wait(select_item)
#     def select_item(self, locator, *, item):
#         element = self.driver.find_element(*locator)
#         s = Select(element)
#         if isinstance(item, str):
#             s.select_by_visible_text(item)
#         elif isinstance(item, int):
#             s.select_by_index(item)
#         else:
#             raise TypeError(f"Invalid Type {item}")
#
#     @wait
#     def select_items(self, locator, *, items):
#         for _item in items:
#             try:
#                 self.select_item(locator, item=_item)
#             except NoSuchElementException:
#                 print(f"Could not find item {_item}")
#                 continue
#
#
# driver = Chrome(r"C:\Users\user\Desktop\training\chromedriver")
# driver.get("file:///C:/Users/user/Desktop/google_drive%20folder/demo.html")
# sleep(5)
#
# s = SeleniumWrapper(driver)
#
# # s.select_item(("id", "standard_cars), item=8)
# # click_element(("link text", "Register"))
# s.select_items(("id", "multiple_cars"), items=['Mercedes', 'Creta', 'BMW', 6 ])     # ,10
#
# # output = Could not find item Creta


####################################################################################################

# from selenium.webdriver import Chrome
# from time import sleep
# from selenium.webdriver.support.select import Select
# import csv
# import re
# from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support.expected_conditions import visibility_of_element_located
# from selenium.webdriver.remote.webelement import WebElement
# from selenium.webdriver.common.action_chains import ActionChains
#
#
# class _visibility_of_element_located(visibility_of_element_located):
#     def __init__(self, locator):
#         super().__init__(locator)
#
#     def __call__(self, driver):
#         result = super().__call__(driver)
#         # Checking if __call__ has returned a WebElement?
#         if isinstance(result, WebElement):
#             return result.is_enabled()
#         return result
#
#
# def enter_text( locator, *, value):
#     driver.find_element(*locator).send_keys(value)
#
#
# def click_element(locator):
#     driver.find_element(*locator).click()
#
#
# def select_item():
#     ...
#
# driver = Chrome(r"C:\Users\user\Desktop\training\chromedriver")
# driver.get(r"http://demowebshop.tricentis.com")
# sleep(5)
#
# click_element(("link text", "Register"))
# sleep(2)
#
# click_element(("id", "gender-male"))
# sleep(2)
#
# enter_text(("id", "FirstName"), value="hello")
# sleep(2)
#
# enter_text(("id", "LastName"), value="world")
# sleep(2)
#
# enter_text(("id", "Email"), value="hello.world@company.com")
# sleep(2)
#
# enter_text(("id", "Password"), value="password123")
# sleep(2)
#
# enter_text(("id", "ConfirmPassword"), value="password123")
# sleep(2)
#
# click_element(("id", "register-button"))
# sleep(2)

# execute..
####################################################################################################
#
# from selenium.webdriver import Chrome
# from time import sleep
# from selenium.webdriver.support.select import Select
# import csv
# import re
# from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support.expected_conditions import visibility_of_element_located
# from selenium.webdriver.remote.webelement import WebElement
# from selenium.webdriver.common.action_chains import ActionChains
#
#
# class _visibility_of_element_located(visibility_of_element_located):
#     def __init__(self, locator):
#         super().__init__(locator)
#
#     def __call__(self, driver):
#         result = super().__call__(driver)
#         # Checking if __call__ has returned a WebElement?
#         if isinstance(result, WebElement):
#             return result.is_enabled()
#         return result
#
#
# # def enter_text( locator, value):
# def enter_text( loctype, locvalue, value):
#     # loctype, locvalue = locator
#     driver.find_element(loctype, locvalue).send_keys(value)
#
# # def enter_text( locator, value):
# def click_element(loctype, value ):
#     # loctype, locvalue = locator
#     driver.find_element(loctype, value).click()
#
#
# def select_item():
#     ...
#
# driver = Chrome(r"C:\Users\user\Desktop\training\chromedriver")
# driver.get(r"http://demowebshop.tricentis.com")
# sleep(5)
#
# click_element("link text", "Register")
# sleep(2)
#
# click_element("id", "gender-male")
# sleep(2)
#
# enter_text("id", "FirstName", "hello")
# sleep(2)
#
# enter_text("id", "LastName", "world")
# sleep(2)
#
# enter_text("id", "Email", "hello.world@company.com")
# sleep(2)
#
# enter_text("id", "Password", "password123")
# sleep(2)
#
# enter_text("id", "ConfirmPassword", "password123")
# sleep(2)
#
# click_element("id", "register-button")
# sleep(2)
#
# # execute.......

#########################################################################################################
#
# from selenium.webdriver.support import wait
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver import Chrome
# from time import sleep
# from selenium.webdriver.support.select import Select
# import csv
# import re
# from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.support.expected_conditions import visibility_of_element_located
# from selenium.webdriver.remote.webelement import WebElement
# from selenium.webdriver.common.action_chains import ActionChains
#
#
# class _visibility_of_element_located(visibility_of_element_located):
#     def __init__(self, locator):
#         super().__init__(locator)
#
#     def __call__(self, driver):
#         result = super().__call__(driver)
#         # Checking if __call__ has returned a WebElement?
#         if isinstance(result, WebElement):
#             return result.is_enabled()
#         return result
#
# def enter_text():
#     ...
#
# def click_element():
#     ...
#
# def select_item():
#     ...
#
# driver = Chrome(r"C:\Users\user\Desktop\training\chromedriver")
# driver.get(r"http://demowebshop.tricentis.com")
# sleep(5)
#
# # print("done")
# driver.find_element("link text", "Register").click()
# sleep(2)
#
# driver.find_element("id", "gender-male").click()
# sleep(2)
#
# driver.find_element("id", "FirstName").send_keys("hello")
# sleep(2)
#
# driver.find_element("id", "LastName").send_keys("world")
# sleep(2)
#
# driver.find_element("id", "Email").send_keys("hello.world@company.com")
# sleep(2)
#
# driver.find_element("id", "Password").send_keys("password123")
# sleep(2)
#
# driver.find_element("id", "ConfirmPassword").send_keys("password123")
# sleep(2)
#
# driver.find_element("id", "register-button").click()
# sleep(2)

# execute

#######################################################################################################


#######################################################################################################
# from selenium.webdriver.support import wait
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver import Chrome
# from time import sleep
# from selenium.webdriver.support.select import Select
# import csv
# import re
# from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.support.expected_conditions import visibility_of_element_located
# from selenium.webdriver.remote.webelement import WebElement
# from selenium.webdriver.common.action_chains import ActionChains
#
#
# class _visibility_of_element_located(visibility_of_element_located):
#     def __init__(self, locator):
#         super().__init__(locator)
#
#     def __call__(self, driver):
#         result = super().__call__(driver)
#         # Checking if __call__ has returned a WebElement?
#         if isinstance(result, WebElement):
#             return result.is_enabled()
#         return result
#
#
# driver = Chrome(r"C:\Users\user\Desktop\training\chromedriver")
# driver.get(r"file:///C:/Users/user/Desktop/google_drive%20folder/progressbar.html")
# sleep(5)
#
# driver.find_element_by_xpath("//button[text()='Click Me']").click()
#
# wait = WebDriverWait(driver, 30)
# v = _visibility_of_element_located(("xpath", "//div[text()='100%']"))
# # print(v)
# # wait.until(v)
#
# # print("done")
#
####################################################################################
#
# from selenium.webdriver import Chrome
# from time import sleep
# from selenium.webdriver.support.select import Select
# import csv
# import re
# from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support.expected_conditions import visibility_of_element_located
# from selenium.webdriver.remote.webelement import WebElement
# from selenium.webdriver.common.action_chains import ActionChains
#
#
# class _visibility_of_element_located(visibility_of_element_located):
#     def __init__(self, locator):
#         super().__init__(locator)
#
#     def __call__(self, driver):
#         result = super().__call__(driver)
#         # Checking if __call__ has returned a WebElement?
#         if isinstance(result, WebElement):
#             return result.is_enabled()
#         return result
#
# def wait(func):
#     def wrapper(*args, **kwargs):       # args = (self, ("id", "multiple_cars"))
#         # instance = args[0]
#         locator = args[0]       # get the inner tuple
#         # Wait (3 Conditions)
#         # wait = WebDriverWait(instance.driver, 10)
#         wait = WebDriverWait(driver, 10)
#         v = _visibility_of_element_located(locator)
#         wait.until(v)
#         return func(*args, **kwargs)        # original func is executed (click_element, enter_text)
#     return wrapper
#
#
# @wait   # enter_text = wait(enter_text)
# def enter_text(locator, *, value):
#     driver.find_element(*locator).send_keys(value)
#
# @wait   # click_element = wait(click_element)
# def click_element(locator):
#     driver.find_element(*locator).click()
#
# @wait       # select_item = wait(select_item)
# def select_item():
#     ...
#
# @wait
# def select_items():
#     ...
#
# driver = Chrome(r"C:\Users\user\Desktop\training\chromedriver")
# driver.get("http://demowebshop.tricentis.com")
# sleep(5)
#
#
# click_element(("link text", "Register"))
# sleep(2)
#
# click_element(("id", "gender-male"))
# sleep(2)
#
# enter_text(("id", "FirstName"), value="hello")
# sleep(2)
#
# enter_text(("id", "LastName"), value="world")
# sleep(2)
#
# enter_text(("id", "Email"), value= "hello.world@company.com")
# sleep(2)
#
# enter_text(("id", "Password"), value="password123")
# sleep(2)
#
# enter_text(("id", "ConfirmPassword"), value= "password123")
# sleep(2)
#
# click_element(("id", "register-button"))
# sleep(2)
#
# # execute

################################################################################################
# from selenium.webdriver import Chrome
# from time import sleep
# from selenium.webdriver.support.select import Select
# import csv
# import re
# from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support.expected_conditions import visibility_of_element_located
# from selenium.webdriver.remote.webelement import WebElement
# from selenium.webdriver.common.action_chains import ActionChains
#
#
# class _visibility_of_element_located(visibility_of_element_located):
#     def __init__(self, locator):
#         super().__init__(locator)
#
#     def __call__(self, driver):
#         result = super().__call__(driver)
#         # Checking if __call__ has returned a WebElement?
#         if isinstance(result, WebElement):
#             return result.is_enabled()
#         return result
#
# def wait(func):
#     def wrapper(*args, **kwargs):       # args = (self, ("id", "multiple_cars"))
#         # instance = args[0]
#         locator = args[0]       # get the inner tuple
#         # Wait (3 Conditions)
#         # wait = WebDriverWait(instance.driver, 10)
#         wait = WebDriverWait(driver, 10)
#         v = _visibility_of_element_located(locator)
#         wait.until(v)
#         return func(*args, **kwargs)        # original func is executed (click_element, enter_text)
#     return wrapper
#
#
# @wait   # enter_text = wait(enter_text)
# def enter_text(locator, *, value):
#     driver.find_element(*locator).send_keys(value)
#
# @wait   # click_element = wait(click_element)
# def click_element(locator):
#     driver.find_element(*locator).click()
#
# @wait       # select_item = wait(select_item)
# def select_item():
#     ...
#
# @wait
# def select_items():
#     ...
#
# driver = Chrome(r"C:\Users\user\Desktop\training\chromedriver")
# driver.implicitly_wait(10)
# driver.get("http://demowebshop.tricentis.com/")
# sleep(5)
#
# register = driver.find_element_by_link_text("Register")
# print(register)  # <selenium.webdriver.remote.webelement.WebElement (session="a8a4353907ab98a6f63a0c6ddae8e4fc", element="a45a5c0a-fa9b-4ba6-853a-c52bc8237c8f")>
# register.click()
#
# print(register)   # <selenium.webdriver.remote.webelement.WebElement (session="a8a4353907ab98a6f63a0c6ddae8e4fc", element="a45a5c0a-fa9b-4ba6-853a-c52bc8237c8f")>

# register.click()



# register = driver.find_element_by_link_text("Register")
# print(register)  # <selenium.webdriver.remote.webelement.WebElement (session="a8a4353907ab98a6f63a0c6ddae8e4fc", element="a45a5c0a-fa9b-4ba6-853a-c52bc8237c8f")>
# register.click()
#
# register = driver.find_element_by_link_text("Register")
# print(register)   # <selenium.webdriver.remote.webelement.WebElement (session="a8a4353907ab98a6f63a0c6ddae8e4fc", element="a45a5c0a-fa9b-4ba6-853a-c52bc8237c8f")>
# register.click()
#
# # <selenium.webdriver.remote.webelement.WebElement (session="a73cfb0cbea145364c37d50cffbe73fd", element="29fe3f30-e8a8-4f99-b2d9-bc080e7bd1f6")>
# # <selenium.webdriver.remote.webelement.WebElement (session="a73cfb0cbea145364c37d50cffbe73fd", element="072eef8f-9de7-4289-b2f2-1e7dd665df66")>

# staleException
# each click generate new id number, and if we use old one then we will get staleException


####################################################################################################
#
# from selenium.webdriver import Chrome
# from time import sleep
# from selenium.webdriver.support.select import Select
# import csv
# import re
# from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support.expected_conditions import visibility_of_element_located
# from selenium.webdriver.remote.webelement import WebElement
# from selenium.webdriver.common.action_chains import ActionChains
#
#
# class _visibility_of_element_located(visibility_of_element_located):
#     def __init__(self, locator):
#         super().__init__(locator)
#
#     def __call__(self, driver):
#         result = super().__call__(driver)
#         # Checking if __call__ has returned a WebElement?
#         if isinstance(result, WebElement):
#             return result.is_enabled()
#         return result
#
# def wait(func):
#     def wrapper(*args, **kwargs):       # args = (self, ("id", "multiple_cars"))
#         # instance = args[0]
#         locator = args[0]       # get the inner tuple
#         # Wait (3 Conditions)
#         # wait = WebDriverWait(instance.driver, 10)
#         wait = WebDriverWait(driver, 10)
#         v = _visibility_of_element_located(locator)
#         wait.until(v)
#         return func(*args, **kwargs)        # original func is executed (click_element, enter_text)
#     return wrapper
#
#
# @wait   # enter_text = wait(enter_text)
# def enter_text(locator, *, value):
#     driver.find_element(*locator).send_keys(value)
#
# @wait   # click_element = wait(click_element)
# def click_element(locator):
#     driver.find_element(*locator).click()
#
# @wait       # select_item = wait(select_item)
# def select_item():
#     ...
#
# @wait
# def select_items():
#     ...
#
# driver = Chrome(r"C:\Users\user\Desktop\training\chromedriver")
# driver.implicitly_wait(10)
# driver.get("http://demowebshop.tricentis.com/")
# sleep(5)
#
#
# box = driver.find_element_by_id("products-orderby")
# s = Select(box)
# s.select_by_visible_text("Name: A to Z")
# sleep(4)
#
# box = driver.find_element_by_id("products-orderby")
# s = Select(box)
# s.select_by_visible_text("Ceated on")
# sleep(4)

# ????????????????????????????????????????????????????????????????????
#########################################################################################

# from selenium.webdriver import Chrome
# from time import sleep
# from selenium.webdriver.support.select import Select
# import csv
# import re
# from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support.expected_conditions import visibility_of_element_located
# from selenium.webdriver.remote.webelement import WebElement
# from selenium.webdriver.common.action_chains import ActionChains
#
#
# class _visibility_of_element_located(visibility_of_element_located):
#     def __init__(self, locator):
#         super().__init__(locator)
#
#     def __call__(self, driver):
#         result = super().__call__(driver)
#         # Checking if __call__ has returned a WebElement?
#         if isinstance(result, WebElement):
#             return result.is_enabled()
#         return result
#
# def wait(func):
#     def wrapper(*args, **kwargs):       # args = (self, ("id", "multiple_cars"))
#         # instance = args[0]
#         locator = args[0]       # get the inner tuple
#         # Wait (3 Conditions)
#         # wait = WebDriverWait(instance.driver, 10)
#         wait = WebDriverWait(driver, 10)
#         v = _visibility_of_element_located(locator)
#         wait.until(v)
#         return func(*args, **kwargs)        # original func is executed (click_element, enter_text)
#     return wrapper
#
#
# @wait   # enter_text = wait(enter_text)
# def enter_text(locator, *, value):
#     driver.find_element(*locator).send_keys(value)
#
# @wait   # click_element = wait(click_element)
# def click_element(locator):
#     driver.find_element(*locator).click()
#
# @wait       # select_item = wait(select_item)
# def select_item():
#     ...
#
# @wait
# def select_items():
#     ...
#
# driver = Chrome(r"C:\Users\user\Desktop\training\chromedriver")
# driver.implicitly_wait(10)
# driver.get("http://demowebshop.tricentis.com/")
# sleep(5)
#
# fnames = driver.find_element_by_xpath("//table[@name='customers']//td[2]")
# names = [fname.text for fname in fnames]
# print(names)
#
# sorted_names = sorted(names)
# print(sorted_names)

# ?????????????????????????????????????????????????????????????????????????????
###################################################################################################



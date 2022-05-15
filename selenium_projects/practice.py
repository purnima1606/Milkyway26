# from selenium.webdriver import Chrome
# from time import sleep
#
# driver = Chrome(r"C:\Users\user\Desktop\training\chromedriver")
# #################################################################################
# driver.get("https://www.monsterindia.com/")
# driver.maximize_window()
# sleep(3)
#
# driver.find_element_by_id("SE_home_autocomplete").send_keys("Python")
# sleep(5)
#
# driver.find_element_by_xpath("(//strong[text()='Python'])[1]").click()
# sleep(5)
#
# driver.find_element_by_xpath("//input[@value='Search']").click()
# sleep(5)
#
# driver.find_element_by_xpath("(//div[@class='job-tittle']/h3/a)[1]").click()
# sleep(5)
#
# handles = driver.window_handles
#
# driver.switch_to_window(handles[1])
#
# driver.find_element_by_xpath(("(//button[text()='APPLY'])[1]").CLICK())
#

###########################################################################################

# driver.get("http://demowebshop.tricentis.com/computing-and-internet")
# driver.maximize_window()
# sleep(3)
#
# driver.find_element_by_xpath("//a[@tittle='Facebook']").click()
# sleep(4)
#
# handles = driver.window_handles
#
# driver.switch_to_window(handles[1])
# sleep(3)
#
# driver.find_element_by_name("email").send_keys("hello.world@company.com")
# driver.close()
#
# driver.switch_to_window(handles[0])
# sleep(3)
# driver.close()

###############################################################################################

# JAVASCRIPT ALERT...........................

# driver.get("http://demowebshop.tricentis.com/computing-and-internet")
# driver.maximize_window()
# sleep(3)
#
# driver.find_element_by_xpath("//input[@value='Search']").click()
# sleep(2)
#
# print(driver.switch_to_alert.text)
#
# driver.switch_to_alert.accept()

# execute properly............

##################################################################################

# JAVASCRIPT CONFIRM.....................

# driver.get("file:///C:/Users/user/Desktop/google_drive%20folder/demo.html")
# driver.maximize_window()
# sleep(3)
#
# elements = driver.find_element_by_xpath("//input[@class='alert']").click()
#
# for item in elements:
#     item.click()
#     sleep(1)
#
#
# driver.find_element_by_id("Delete").click()
# sleep(2)
#
# driver.switch_to_alert.accept()
# sleep(2)
#
# driver.find_element_by_id("Delete").click()
# sleep(2)
#
# driver.switch_to_alert.accept()
# sleep(2)


#######################################################################################

# FILE UPLOAD..................
# upload your CV on naukri.com ...............................................

# driver.get("https://www.naukri.com/")

# driver.maximize_window()
# sleep(5)
#
# driver.find_element_by_xpath("input[@type='file']").send_keys("hello.docx")

#########################################################################

# FILE DOWNLOAD...................................




#############################################################################################

# AUTHENTICATION....................

# driver.get("https://the-internet.herokuapp.com/basic_auth")
# sleep(5)
#
# driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")


# execute properly

##############################################################################################

# MODEL WINDOW OR HIDDEN DIVISION POPUP.................

######################################################################################################

# date
##############################################################################################

# .........................synchronization................................................


# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support.expected_conditions import visibility_of_element_located
# from selenium.webdriver.remote.webelement import WebElement
#
# driver.get("file:///C:/Users/user/Desktop/google_drive%20folder/loading.html")
#
#
# class _visibility_of_element_located(visibility_of_element_located):         # inherit visibility_of_element_located class in child class _visibility_of_element_located
#     def __call__(self, driver):
#         result = super().__call__(driver)                    # calling parent class(object class) __call__ method and pass driver as an argument:
#         if isinstance(result, WebElement):
#             print("checking for enable")
#             return result.is_enabled()
#         return result
#
#
# wait = WebDriverWait(driver, 200)
# v = _visibility_of_element_located(("name", "fname"))
# wait.until(v)
# driver.find_element_by_name("fname").send_keys("Hello")
# execute properly
############################################
# ................................ IS_VISIBLE_ENABLE (USING DECORATOR , ALTERNATE SOLUTION).........................
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select

driver.get("file:///C:/Users/user/Desktop/google_drive%20folder/loading.html")


class _visibility_of_element_located(visibility_of_element_located):         # inherit visibility_of_element_located class in child class _visibility_of_element_located
    def __init__(self, locator):
        super().__init__(locator)

    def __call__(self, driver):
        result = super().__call__(driver)                    # calling parent class(object class) __call__ method and pass driver as an argument:
        # checking if __call__ has returned a WebElement?
        if isinstance(result, WebElement):
            print("checking for enable")
            return result.is_enabled()
        return result


def wait(func):
    def wrapper(*args, **kwargs):                 # args = (self, ("id", "multiple_cars"))
        # instance = args[0]                      # instance == driver
        locator = args[1]                         # get the inner tuple
        print('Calling wait decorator')
        print('    args: ', args, '    kwargs: ', kwargs)
        w = WebDriverWait(driver, 30)
        v = _visibility_of_element_located(locator)
        w.until(v)
        return func(*args, **kwargs)        # original func is executed (click_element, enter_text)
    return wrapper


@wait           # enter_text = wait(enter_text)
def enter_text(locator, *, value):
    driver.find_element(*locator).send_keys(value)


@wait          # click_element = wait(click_element)
def click_element(locator):
    driver.find_element(*locator).click()


@wait       # select_item = wait(select_item)
def select_item(locator, *, item):
    element = driver.find_elemet(*locator)
    s = Select(element)
    if isinstance(item, str):
        s.select_by_visible_text(item)
    elif isinstance(item, int):
        s.select_by_index(item)
    else:
        raise TypeError(f"Invalid Type {item} ")

    #s.select_by_visible_text(item)


click_element(("link text", "Register"))
# select_items(("id", "multiple_cars"), items =["Mercedes", "Creta", "BMW", 10])


"""


###############################################################
# ?????????????????????????????????????????????????????????????????????

# from selenium import webdriver
# from selenium.webdriver.remote.webelement import WebElement
# # from selenium.webdriver import Chrome
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support.expected_conditions import visibility_of_element_located
# driver = webdriver.Chrome("./chromedriver1.exe")
#
# driver.get(r"http://demowebshop.tricentis.com/")
#
#
# def wait(func):
#     def wrapper(*args, **kwargs):
#         locator = args[0]
#         print('Calling wait decorator')
#         print('    args: ', args, '    kwargs: ', kwargs)
#         w = WebDriverWait(driver, 30)
#         v = _visibility_of_element_located(locator)
#         w.until(v)
#         return func(*args, **kwargs)
#     return wrapper
#
#
# class _visibility_of_element_located(visibility_of_element_located):
#     def _call_(self, driver):              # Element is loaded in dom
#         print('Calling visibility')          # Element is visible
#         result = super()._call_(driver)    # Element is enabled
#         print('    ', result)
#         if isinstance(result, WebElement):   # if all these 3 conditions are true, Then only "Until" method will run
#             return result.is_enabled()       # if False , "Until" method will wait for Max Timeout Limit
#         else:                                # Until method checks the conditions every 0.5 seconds
#             return False
#
#
# @wait
# def click_element(locator):
#     print('Calling click, parameter : locator ')
#     print('   locator: ', locator)
#     driver.find_element(*locator).click()
#
#
# @wait
# def enter_element(locator, value):
#     print('Calling enter, parameter : locator, value')
#     print('    locator: ', locator, '    value: ', value)
#     driver.find_element(*locator).clear()
#     driver.find_element(*locator).send_keys(value)
#
#
# click_element(('xpath', '//a[@class="ico-register"]'))
# print()
# print()
# click_element(('id', 'gender-male'))
# print()
# print()
# enter_element(('id', 'FirstName'), value='Preetham')
# print()
# print()
# enter_element(('id', 'LastName'), value='S R')
# print()
# print()
# enter_element(('id', 'Email'), value='p2@gmail.com')
# print()
# print()
# enter_element(('id', 'Password'), value='secret')
# print()
# print()
# enter_element(('id', 'ConfirmPassword'), value='secret')
# print()
# print()
# click_element(('id', 'register-button'))
#
# driver.quit()


############################################################
# wait(10)

# driver.get("file:///C:/Users/user/Desktop/google_drive%20folder/loading.html")
# driver.maximize_window()
# sleep(4)
#
# driver.implicitly_wait(10)
#
# first_name = driver.find_element_by_name("fname")
# first_name.send_keys("hello")

########################################################################################################

# WAIT FOR PROGRESSBAR TO COMPLETE 100% IN DEMO HTML PAGE


# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions
#
# driver.get("file:///C:/Users/user/Desktop/google_drive%20folder/progressbar.html")
# sleep(2)
#
# driver.find_element_by_xpath("//button[text()='Click Me']").click()
# wait = WebDriverWait(driver, 10)
#
# wait.until(expected_conditions.visibility_of_element_located(("xpath", "//div[text()='100%']")))
# print("Done!")


################################################################################################

# SELECT ELEMENT..........................
# IS_MULTIPLE...................
# from selenium.webdriver.support.select import Select
#
# driver.get("file:///C:/Users/user/Desktop/google_drive%20folder/demo.html")
# driver.maximize_window()
# sleep(4)
#
# a_box = driver.find_element_by_id("multiple_cars")
#
# select = Select(a_box)
#
# print(select.is_multiple)   # True

##########################################################################################################
# ALL SELECTED OPTION ....................

# from selenium.webdriver.support.select import Select
#
# driver.get("file:///C:/Users/user/Desktop/google_drive%20folder/demo.html")
# driver.maximize_window()
# sleep(4)
#
# a_box = driver.find_element_by_id("multiple_cars")
#
# select = Select(a_box)
#
# select.select_by_visible_text("Mercedes")
# select.select_by_visible_text("Audi")
# select.select_by_visible_text("Toyota")
#
# all_selected_options = select.all_selected_options
#
# for item in all_selected_options:
#     print(item.text)   # Audi   #Mercedes #Toyota


#############################################################################################
# SELECTING ALL ITEM IN MULTIPLE SELECT

# from selenium.webdriver.support.select import Select
#
# driver.get("file:///C:/Users/user/Desktop/google_drive%20folder/demo.html")
# driver.maximize_window()
# sleep(4)
#
# a_box = driver.find_element_by_id("multiple_cars")
#
# select = Select(a_box)
# all_options = select.options
#
# items = [item.text for item in all_options]
#
# for item in items:
#     select.select_by_visible_text(item)
#     sleep(2)

# execute properly......

#######################################################################################################

# DESELECT_BY_VISIBLE_TEXT.....................
# DESELECT_BY_INDEX.................................
# DESELECT_BY_VALUE...........................
#
# from selenium.webdriver.support.select import Select
#
# driver.get("file:///C:/Users/user/Desktop/google_drive%20folder/demo.html")
# driver.maximize_window()
# sleep(4)
#
# a_box = driver.find_element_by_id("multiple_cars")
#
# s = Select(a_box)
#
# s.deselect_by_visible_text("Audi")
# sleep(2)
#
# s.deselect_by_index(8)
# sleep(2)
#
# s.deselect_by_visible_text("Mercedes")
# sleep(2)

# execute properly.......................       # o\p = show error

########################################################################################
# SELECTING MULTIPLE ITEM IN MULTIPLE_SELECT..............................

# from selenium.webdriver.support.select import Select
#
# driver.get("file:///C:/Users/user/Desktop/google_drive%20folder/demo.html")
# driver.maximize_window()
# sleep(4)
#
# a_box = driver.find_element_by_id("multiple_cars")
#
# select = Select(a_box)
#
# select.select_by_visible_text("Mercedes")
# sleep(1)
# select.select_by_visible_text("Audi")
# sleep(1)
# select.select_by_visible_text("Toyota")
# sleep(1)

# execute properly.....

##########################################################
# PRINT INDEX AT WATCH THE "MERCEDES" IS PRESENT........................

# from selenium.webdriver.support.select import Select
#
# driver.get("file:///C:/Users/user/Desktop/google_drive%20folder/demo.html")
# driver.maximize_window()
# sleep(4)
#
# a_box = driver.find_element_by_id("multiple_cars")
#
# select = Select(a_box)
# all_options = select.options
#
# items = [item.text for item in all_options]
#
# for index, item in enumerate(items):
#     if item == "Mercedes":
#         print(f"{item} is present at {index}")     # Mercedes is present at 7

######################################################################################

# SELECTING EACH ITEM IN THE LIST BOX ONE BY ONE IN REVERSE ORDER.................

# from selenium.webdriver.support.select import Select
#
# driver.get("file:///C:/Users/user/Desktop/google_drive%20folder/demo.html")
# driver.maximize_window()
# sleep(4)
#
# a_box = driver.find_element_by_id("multiple_cars")
#
# select = Select(a_box)
# all_options = select.options
#
# # for item in all_options[::-1]:
# for item in reversed(all_options):
#     select.select_by_visible_text(item.text)
#     sleep(1)

# execute properly...................................................

#########################################################################################

# SELECT LAST ITEM OF THE LIST BOX..................

# from selenium.webdriver.support.select import Select
#
# driver.get("file:///C:/Users/user/Desktop/google_drive%20folder/demo.html")
# driver.maximize_window()
# sleep(4)
#
# a_box = driver.find_element_by_id("multiple_cars")
#
# s = Select(a_box)
# all_options = s.options
#
# items = [item.text for item in all_options]
# s.select_by_visible_text(items[-1])

# execute properly.........................

###################################################################################################

# SELECTING EACH ITEM IN THE LIST BOX ONE BY ONE...................................

# from selenium.webdriver.support.select import Select
#
# driver.get("file:///C:/Users/user/Desktop/google_drive%20folder/demo.html")
# driver.maximize_window()
# sleep(4)
#
# a_box = driver.find_element_by_id("multiple_cars")
#
# select = Select(a_box)
# all_options = select.options
#
# for item in all_options:
#     select.select_by_visible_text(item.text)
#     sleep(1)

# execute properly...................................................

#####################################################################################################
# OPTIONS.......................

# from selenium.webdriver.support.select import Select
#
# driver.get("file:///C:/Users/user/Desktop/google_drive%20folder/demo.html")
# driver.maximize_window()
# sleep(4)
#
# a_box = driver.find_element_by_id("multiple_cars")
#
# select = Select(a_box)
# all_options = select.options
#
# for item in all_options:
#     print(item.text)   # Select car: # Audi # BMW # Ford # Honda # Jaguar #Land Rover
#     sleep(1)

#########################################################################################################

# SELECT_BY_VALUE.........................

# from selenium.webdriver.support.select import Select
#
# driver.get("file:///C:/Users/user/Desktop/google_drive%20folder/demo.html")
# driver.maximize_window()
# sleep(4)
#
# a_box = driver.find_element_by_id("standard_cars")
#
# select = Select(a_box)
# all_options = select.options
#
# select.select_by_value("jgr")
# sleep(1)
#
# select.select_by_value("vol")
# sleep(1)

# execute properly.......................
#########################################################################################

# SELECT_BY_INDEX.........................

# from selenium.webdriver.support.select import Select
#
# driver.get("file:///C:/Users/user/Desktop/google_drive%20folder/demo.html")
# driver.maximize_window()
# sleep(4)
#
# a_box = driver.find_element_by_id("standard_cars")
#
# select = Select(a_box)
# all_options = select.options
#
# select.select_by_index(4)
# sleep(1)
#
# select.select_by_index(8)
# sleep(1)

# execute properly.......................
#########################################################################################

# SELECT_BY_VISIBLE_TEXT.........................

# from selenium.webdriver.support.select import Select
#
# driver.get("file:///C:/Users/user/Desktop/google_drive%20folder/demo.html")
# driver.maximize_window()
# sleep(4)
#
# a_box = driver.find_element_by_id("standard_cars")
#
# select = Select(a_box)
# all_options = select.options
#
# select.select_by_visible_text("Audi")
# sleep(1)
#
# select.select_by_visible_text("Mercedes")
# sleep(1)

# execute properly.......................
#########################################################################################
# .............................LOCATING MULTIPLE ELEMENTS................................
# .................................get_attribute.................................
# ...............................ALT TAG.............................................

# from selenium.webdriver.support.select import Select
#
# driver.get("https://services.smartbear.com/samples/TestComplete14/smartstore")
# driver.maximize_window()
# sleep(4)
#
# images = driver.find_elements_by_xpath("//img")
# for image in images:
#     print(image.get_attribute("alt"))
#     sleep(0.5)
"""
Your store name
Picture for category Mobile phone
Picture for category Sports
Picture for category Furniture
Picture for category Sunglasses
Picture for category Soccer
Picture for category Basketball
Picture for category Golf
Picture for category Fashion
Picture for category Gaming
Picture for category Watches
Picture for category Gift Cards
Picture of CHRONOGRAPH watch
Picture of Touch Expert Solar
Picture of Mechanical Automatic 
Picture of The tablet
Picture of Podium Big Size
Picture of Accessories for unlimited gaming experience
Picture of Sneaker shoes
Picture of Lounge Chair
Picture of Cube chair

"""

##############################################################################################
#


# from selenium.webdriver.support.select import Select

# driver.get("https://www.python.org")
# driver.maximize_window()
# sleep(4)
#
# links = driver.find_elements_by_xpath("//a")
# urls = []
#
# for link in links:
#     link_text = link.text
#
#     if "python" in link_text:
#         value_href = link.get_attribute("href")
#         urls.append((value_href, link_text))
#
# for url in urls:
#     print(url)

"""
('https://docs.python.org/', 'docs.python.org')
('https://jobs.python.org/', 'jobs.python.org')
('https://mail.python.org/mailman/listinfo/python-dev', 'python-dev list')
"""

####################################################################################################
# ................PRINT LINK TEXT OF ALL THE LINKS......................

# from selenium.webdriver.support.select import Select
#
# driver.get("https://www.python.org")
# driver.maximize_window()
# sleep(4)
#
# links = driver.find_elements_by_xpath("//a")
# all_links = []
#
# for link in links:
#     all_links.append((link.text.strip()))
#
#
# for url in all_links:
#     print(url)

# execute properly.....................

#############################################################################################
# ............................ALTERNATE SOLUTION USING LIST COMPREHENSION........................

# driver.get("https://www.python.org")
# driver.maximize_window()
# sleep(4)
#
# links = driver.find_elements_by_xpath("//a")
# all_links = [link.text.strip() for link in links]
#
# for link in all_links:
#     print(link)

# execute properly..........................

##############################################################################################
# LIST OF LINK TEXT OF ALL THE LINKS IF THE TEXT CONTAINS "PYTHON" WORD IN IT..................

# driver.get("https://www.python.org")
# driver.maximize_window()
# sleep(4)
#
# links = driver.find_elements_by_xpath("//a")
# python_links = []
#
# for link in links:
#     link_of_link = link.text
#     # print(link_of_link)
#     if "python" in link_of_link:
#         python_links.append(link.text.strip())
#
# for link in python_links:
#     print(link)

"""
docs.python.org
jobs.python.org
python-dev list
"""

#######################################################################################################

# 5 4 3 2 1
#   4 3 2 1
#    3 2 1
#      2 1
#        1
n = 5
a = 1
while n >=1:
    for i in range(n, 1):
        print(" "*a)
        print(i,end=" ")
        a += 1
        n -= 1
















































































































































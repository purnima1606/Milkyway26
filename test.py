from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.support.select import Select

driver = Chrome(r"C:\Users\user\Desktop\training\chromedriver")
# driver.get("https://www.facebook.com")
# driver.maximize_window()
# sleep(4)

# print(driver.title)  # Facebook – log in or sign up
#
# print(driver.current_url) # https://www.facebook.com/
#
# user_name = driver.find_element("id", "email")
#
# # print(user_name.is_displayed)
# print(user_name.is_displayed())     # True
# # print(user_name.is_enabled)
# print(user_name.is_enabled())       # True
#
# user_name.send_keys("purnimasingh26th@gmail.com")
#
# user_password = driver.find_element("id", "pass")
#
# # print(user_name.is_displayed)

# ******* status check *************
# print(user_password.is_displayed())     # True
# # print(user_name.is_enabled)

#  *********** check status **********
# print(user_password.is_enabled())       # True
#
# user_password.send_keys("purnima")
#
# # View the passwoed
#
# # driver.find_element("xpath", "//input[@type='text']").click()
# # sleep(3)

# ************************ IMPLICIT WAIT **********************8

# driver.implicitly_wait(10)       # SECONDS
#
# assert "Facebook – log in or sign up" == driver.title
#
# user_name = driver.find_element("id", "email")
# user_name.send_keys("purnimasingh26th@gmail.com")
#
# user_password = driver.find_element("id", "pass")
# user_password.send_keys("purnima")


# ****************** EXPLICITY WAIT ******************
# driver.get("https://www.expedia.com")
# driver.implicitly_wait(5)
# driver.maximize_window()
# # sleep(2)
#
# driver.find_element("xpath", "//span[text()='Flights']").click()
# # sleep(4)
#
# driver.find_element("xpath","//button[@aria-label='Leaving from']").click()
# driver.find_element("id", "location-field-leg1-origin").send_keys("Indianapolis, IN (IND-Indianapolis Intl.)")


# sleep(2)
#
# driver.find_element("xpath", "//button[@aria-label='Going to']").send_keys("San Francisco, CA (SFO-San Francisco Intl.)")
# sleep(2)
#
# driver.find_element("id", "d1-btn").send_keys("16 june")
# sleep(2)


# inputbox_class = driver.find_element("xpath", "//input")
# print(len(inputbox_class))        # object

# **********************************************************************
driver.get("file:///C:/Users/user/Desktop/google_drive%20folder/demo.html")
# driver.implicitly_wait(10)
driver.maximize_window()


# list_box = driver.find_element("id", "standard_cars")
# list_box = driver.find_element("id", "multiple_cars")


# select = Select(list_box)

# all_options = select.options


# for i in all_options:
#     select.select_by_visible_text(i.text)
#     sleep(2)
#     # print(i.text)
#


# for i in all_options[::-1]:
#     print(i.text)
#     select.select_by_visible_text(i.text)
#     sleep(2)

# for i in reversed(all_options):
#     # print(i.text)
#     select.select_by_visible_text(i.text)
#     sleep(2)

# items = [item.text for item in all_options ]
#
# select.select_by_visible_text(items[-1])
# print(items[-1])


# for index, item in enumerate(items):
#     if item == "Mercedes":
#         print(f"index of {item} is {index}")             # index of Mercedes is 7


# select.select_by_visible_text("Audi")
# sleep(2)
# first_selected =select.first_selected_option
# print(first_selected.text)       # Audi


# select.select_by_visible_text("Audi")
# sleep(1)
# select.select_by_visible_text("BMW")
# sleep(1)
#
# all_selected = select.all_selected_options
# # print(all_selected)    # not posible
#
# for i in all_selected:
#     print(i.text)       # Audi , BMW
#     sleep(2)



# print(select.is_multiple)
# select.deselect_all()


# print(select.is_multiple)


# select.select_by_index(2)
# select.select_by_index(3)
# select.select_by_index(4)
# select.select_by_index(5)
# select.select_by_index(6)


list_box = driver.find_element("id", "multiple_cars")
select = Select(list_box)

select.select_by_visible_text("Audi")
sleep(2)

select.deselect_by_visible_text("Audi")
sleep(2)

print(select.is_multiple)

# **************************************************************************************************************************************
""" decorator is a function which is take an argument as a function and add some funcrionality without modifiying original function
"""
# def sub(a,b)

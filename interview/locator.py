""" xpath """

# pep jeans
# from selenium.webdriver import Chrome
# from time import sleep
#
# driver = Chrome(r"C:\Users\user\Desktop\training\chromedriver")
# driver.get("https:\\www.myntra.com\\boys-tshirt")
# # driver.get("https:\\www.myntra.com")
# driver.maximize_window()
# sleep(2)
#
# driver.find_element_by_xpath("(//label[@class='vertical-filters-label common-customCheckbox'])[4]").click()
# sleep(6)
#
# brands = driver.find_elements_by_xpath("//h3[@class='product-brand']")
# sleep(5)
#
# for brand in brands:
#     print(brand.text)

# ????????????????????????????????????????????????????????????????????
# # driver.find_element_by_xpath("//input[@class='desktop-searchBar']").send_keys("boys-tshirt")
# # sleep(2)
#
# # brand = driver.find_element_by_xpath("//span[@class='myntraweb-sprite filter-search-iconSearch sprites-search']").send_keys("pip-jeans")
# driver.find_element_by_xpath("//span[@class='myntraweb-sprite filter-search-iconSearch sprites-search']/..//input[@value='Pepe Jeans']").click()
# sleep(2)
#
# # driver.brand.click()
# driver.find_element_by_xpath("//input[@value='Pepe Jeans']").click
#
# sleep(4)

# current_title = driver.title
# print(current_title)
#
# url = driver.current_url
# print(url)


# ********************************************************************************************************8

# from selenium.webdriver import Chrome
# from time import sleep
#
# driver = Chrome(r"C:\Users\user\Desktop\training\chromedriver")
# driver.get("file:///C:/Users/user/Desktop/google_drive%20folder/demo.html")
# driver.maximize_window()
# sleep(2)
#
# elements = ['Java', 'Ruby', 'Perl', 'Python', 'C#', 'JavaScript']
#
# for element in elements:
#     xpath_ = f"//td[text()='{element}']/..//input[@name='download']"
#     driver.find_element_by_xpath(xpath_).click()
#     sleep(1)
#

# driver.find_element_by_xpath("//td[text()='Java']/..//input[@name='download']").click()
# sleep(2)
#
# driver.find_element_by_xpath("//td[text()='Ruby']/..//input[@name='download']").click()
# sleep(2)
#
# driver.find_element_by_xpath("//td[text()='Perl']/..//input[@name='download']").click()
# sleep(2)
#
# driver.find_element_by_xpath("//td[text()='Python']/..//input[@name='download']").click()
# sleep(2)
#
# driver.find_element_by_xpath("//td[text()='C#']/..//input[@name='download']").click()
# sleep(2)
#
# driver.find_element_by_xpath("//td[text()='JavaScript']/..//input[@name='download']").click()
# sleep(2)


# *******************************************************************************************************
# from selenium.webdriver import Chrome
# from time import sleep
#
# driver = Chrome(r"C:\Users\user\Desktop\training\chromedriver")
# driver.get("http:\\www.python.org\download")
# driver.maximize_window()
# sleep(3)
#
# driver.find_element_by_xpath("//a[text()='Python 3.10.3']/../..//a[text()='Release Notes']").click()
# sleep(4)

# ***********************************************************************************************************
# from selenium.webdriver import Chrome
# from time import sleep
#
# driver = Chrome(r"C:\Users\user\Desktop\training\chromedriver")
# driver.get("http://demowebshop.tricentis.com/books")
# driver.maximize_window()
# sleep(2)
#
# books = ['Fiction', 'Computing and Internet', 'Health Book']
#
# for book in books:
#     xpath_ = f"//a[text()='{book}']/../..//input[@value='Add to cart']"
#     driver.find_element_by_xpath(xpath_).click()
#     sleep(0.5)
#
# sleep(4)
# # click on shopping cart
# driver.find_element("xpath", "//span[text()='Shopping cart']").click()
#
# # click on checkbox
# # driver.find_element_by_xpath("//a[text()='Fiction']/../..//input[@type='checkbox']").click()
# # sleep(4)

# user input
# for book in books:
#     xpath_ = driver.find_element("xpath", f"//a[text()='{book}']/../..//input[@type='checkbox']")
#     xpath_.click()
#     sleep(0.5)

# ***************************************************************************************************
# from selenium.webdriver import Chrome
# from time import sleep
#
# driver = Chrome(r"C:\Users\user\Desktop\training\chromedriver")
# driver.get("http://demowebshop.tricentis.com/")
# driver.maximize_window()
# sleep(4)
#
# ratings = ["Excellent", "Good", "Poor", "Very bad"]
#
# for rating in ratings:
#     xpath_ = driver.find_element_by_xpath(f"//label[text()='{rating}']/..//input[@type='radio']")
#     xpath_.click()
#     sleep(1)
#

# *************************************************************************************************************
# from selenium.webdriver import Chrome
# from time import sleep
#
# driver = Chrome(r"C:\Users\user\Desktop\training\chromedriver")
# driver.get("http://demowebshop.tricentis.com/books")
# driver.maximize_window()
# sleep(2)
#
# expected_prices ={"Health Book":10.00, "Science":51.00, "Fiction":24.00, "Computing and Internet":100.00}
#
# for book, expected_price in expected_prices.items():
#     xpath_ = driver.find_element_by_xpath(f"//a[text()='{book}']/../..//span[@class='price actual-price']")
#     sleep(2)
#     actual_price = xpath_.text
#     # print(actual_price)
#     assert float(actual_price) == expected_price, "Fail"
#         # print("pass")
    # else:
    #     print(book, expected_price, actual_price)

# ******************************************************************************************************************8


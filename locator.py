"""  LOCATORS """
#1.Name
#2.Id
#3.Class
#4.Linktext
#5.Partiallinktext
#6.Css
#7.Tag name
#8.xpath

from selenium.webdriver import Chrome
from time import sleep

# /session/{session id}/window/maximize
driver = Chrome(r"C:\Users\user\Desktop\training\chromedriver")


# /session/{session id}/url --> POST
driver.get("http://demowebshop.tricentis.com/")

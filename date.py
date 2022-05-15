from selenium.webdriver import Chrome
from time import sleep
import re
# /session/{session id}/window/maximize
driver = Chrome(r"C:\Users\user\Desktop\training\chromedriver")
#sleep(3)

# /session/{session id}/url --> POST
driver.get("http://www.goibibo.com")
sleep(5)

driver.find_element_by_xpath("//span[text()='Departure']").click()
sleep(5)

#driver.find_element_by_xpath("//div[text()='may 2022']/../..//p[text()='26']").click()
#sleep(2)

#month = "september 2022"
#day = "26"

def select_date(month, day):
    for _ in range(12):
        try:
            driver.find_element_by_xpath(f"//div[text()='{month}']/../..//p[text()='{day}']").click()
            break
        except NoSuchElementException:
            driver.find_element_by_xpath("//span[@aria_lable='Next Month']").click()
            sleep(1)
            continue


print(select_date("may 2022", "26"))




        


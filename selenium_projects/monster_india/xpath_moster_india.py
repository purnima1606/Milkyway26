from selenium.webdriver import Chrome
from time import sleep
import re

driver = Chrome(r"C:\Users\user\Desktop\training\chromedriver")

driver.get("https://www.monsterindia.com/")
driver.maximize_window()
sleep(2)

driver.find_element_by_xpath("//input[@id='SE_home_autocomplete']").send_keys("python")
sleep(2)

driver.find_element_by_xpath("//div[@class='home_ac']").click()
sleep(1)

driver.find_element_by_xpath("//span[text()='Close']").click()
sleep(3)

# driver.find_element_by_xpath("//input[@id='SE_home_autocomplete_location']").send_keys("bangalore")
# sleep(2)
#
# driver.find_element_by_xpath("//span[text()='Bengaluru / Bangalore']").click()
#
# driver.find_element_by_xpath("//div[@class='multiselect__select modal-ref-class']").click()
# driver.find_element_by_xpath("//span[text()='2 Years']").click()


# driver.find_element_by_xpath("//input[@value='Search']").click()
#
# # print the job titles of all the jobs in monsterindia.com search results
# job_titles = driver.find_elements_by_xpath("//div[@class='job-tittle']/h3/a")
#
# for job_title in job_titles:
#     print(job_title.text)
#     sleep(1)

# MOVE_TO_ELEMENT..................

from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

driver = Chrome(r"C:\Users\user\Desktop\training\chromedriver")
driver.get("https://www.monsterindia.com")
driver.maximize_window()
sleep(5)

actions = ActionChains(driver)

jobs_search = driver.find_element_by_xpath("//a[text()='Job search']")

actions.move_to_element(jobs_search).perform()
sleep(2)

jobs_by_skills = driver.find_element_by_xpath("//a[text()='Job by Skills']")

actions.move_to_element(jobs_by_skills).perform()
sleep(2)

python_jobs = driver.find_element_by_xpath("//a[contains(text(),'Python Jobs')]")
actions.move_to_element(python_jobs).perform()
sleep(3)


python_jobs.click()

# MOVE_TO_ELEMENT..................

from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

driver = Chrome(r"C:\Users\user\Desktop\training\chromedriver")
driver.get("https://www.myntra.com")
driver.maximize_window()
sleep(5)

actions = ActionChains(driver)

profile = driver.find_element_by_xpath("//span[text()='Profile']")

# mouse over on profile...
actions.move_to_element(profile).perform()
sleep(5)


driver.find_element_by_xpath("//a[text()='login/Signup']").click()
sleep(5)

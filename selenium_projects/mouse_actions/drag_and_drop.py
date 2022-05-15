from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

driver = Chrome(r"C:\Users\user\Desktop\training\chromedriver")
driver.get("https://crossbrowsertesting.github.io/drag-and-drop.html")
driver.maximize_window()
sleep(5)

# store "box A"
source_element = driver.find_element_by_id("draggable")

#
target_element = driver.find_element_by_id("droppable")

actions = ActionChains(driver)

actions.drag_and_drop(source_element, target_element).perform()
sleep(3)

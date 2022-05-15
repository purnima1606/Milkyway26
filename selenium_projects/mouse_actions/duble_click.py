from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

driver = Chrome(r"C:\Users\user\Desktop\training\chromedriver")
driver.get("file:///C:/Users/user/Desktop/google_drive%20folder/demo.html")
driver.maximize_window()
sleep(5)

actions = ActionChains(driver)

click_me = driver.find_element_by_xpath("//button[text()='Double-click me']")

actions.double_click(click_me).perform()


# .........................execute properly.........................

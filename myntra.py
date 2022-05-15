
from selenium.webdriver import Chrome
from time import sleep

# /session/{session id}/window/maximize
driver = Chrome(r"C:\Users\user\Desktop\training\chromedriver")
sleep(3)

# /session/{session id}/url --> POST
driver.get("https://www.myntra.com/")
sleep(3)

# /session/{session id}/window/maximize
driver.maximize_window()
sleep(3)

# /session/{session id}/window/minimize
driver.minimize_window()
sleep(3)

driver.maximize_window()
sleep(3)

# /session/{session id}/title
current_title = driver.title

# /session/{session id}/url
url = driver.current_url

#/session/{sessionid}/window
driver.close()

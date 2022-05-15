
from selenium.webdriver import Chrome
from time import sleep

# /session/{session id}/window/maximize
driver = Chrome(r"C:\Users\user\Desktop\training\chromedriver")
sleep(3)

# /session/{session id}/url --> POST
driver.get("https://www.amazon.in/?tag=admpdesktopin-21&ref=pd_sl_a05EB5943DD9437F7D1D7DDCF2/")
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
uel = driver.current_url

#/session/{sessionid}/window
driver.close()

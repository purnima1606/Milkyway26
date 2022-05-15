from selenium.webdriver import Chrome
from time import sleep

# /session/{session id}/window/maximize
driver = Chrome(r"C:\Users\user\Desktop\training\chromedriver")
sleep(3)

# /session/{session id}/url --> POST
driver.get("http://demowebshop.tricentis.com/")
sleep(3)

# /session/{session id}/window/maximize
driver.maximize_window()
sleep(3)

# /session/{session id}/window/minimize
driver.minimize_window()
sleep(3)

# /session/{session id}/window/maximize
driver.maximize_window()
sleep(3)

# /session/{session id}/title
current_title = driver.title
print(current_title)

# /session/{session id}/url
url = driver.current_url
print(url)

#/session/{sessionid}/window
driver.close()




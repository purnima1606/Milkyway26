from selenium.webdriver import Chrome
from time import sleep

driver = Chrome(r"C:\Users\user\Desktop\training\chromedriver")

driver.get("https:\\www.google.com")
sleep(2)

driver.maximize_window()
sleep(2)

# driver.minimize_window()
# sleep(2)
#
# driver.refresh()
# sleep(2)
#
# driver.maximize_window()
# sleep(2)
#
# current_title = driver.title
# print(current_title)
#
# url = driver.current_url
# print(url)

driver.quit()

# driver.close()

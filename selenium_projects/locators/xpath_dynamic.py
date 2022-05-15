from selenium.webdriver import Chrome
from time import sleep

driver = Chrome(r"C:\Users\user\Desktop\training\chromedriver")

driver.get("file:///C:/Users/user/Desktop/google_drive%20folder/demo.html")
driver.maximize_window()
sleep(2)

languages = ["Ruby", "Java", "Perl",	"Python", "C#", "JavaScript"]
for language in languages:
    _xpath = f"//td[text()='{language}']/..//input[@name='download']"
    driver.find_element_by_xpath(_xpath).click()
    sleep(4)

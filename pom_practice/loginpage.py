from selenium.webdriver import Chrome
from time import sleep

#
# driver = Chrome(r"C:\Users\user\Desktop\training\chromedriver")
# driver.get("http://demowebshop.tricentis.com/")
# driver.maximize_window()
# sleep(2)

class LoginPage:
    textbox_username= "Email"
    textbox_password = "Password"
    textbox_login = "//a[text()='Log in']"
    # textbox_logout =

    def getUsername(self, username):

        self.driver.find_element("id", self.textbox_username).send_keys(username)

    def getPassword(self, password):

        self.driver.find_element("id", self.textbox_password).send_keys(password)

    def clickLogin(self):

        self.driver.find_element("xpath", self.textbox_login).click()

    # def clickLogout(self):

        # self.driver.find_element("","").click



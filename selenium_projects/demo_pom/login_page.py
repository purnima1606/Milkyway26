from seleniumWrapper import SeleniumWrapper
class Loginpage(SeleniumWrapper):
    _txt_email = ("id", "Email")
    _txt_password = ("id", "Password")
    _clk_login = ("xpath", "//input[@value='Log in']")

    def enter_login_email(self,email):
        self.enter_text(self._txt_email, value = email)

    def enter_login_password(self,password):
        self.enter_text(self._txt_password, value = password)

    def clk_login_button(self):
        self.click_element(self._clk_login)

from pytest import mark
from homepage import Homepage
from login_page import Loginpage
headers = "email, password"
data = [
    ("bill.gates@company.com", "Password123"),
    ("hello.world@company.com", "Password123")
]
@mark.parametrize(headers,data)
def test_login_positive(setup,email,password):
    hp = Homepage(setup)
    hp.home_click_login()
    lp = Loginpage(setup)
    lp.enter_login_email(email)
    lp.enter_login_password(password)
    lp.clk_login_button()




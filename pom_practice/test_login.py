from pytest import mark
from loginpage import LoginPage

@mark.parameterize()
def test_login(setup):

        lp= LoginPage(setup)

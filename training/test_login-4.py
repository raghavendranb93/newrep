from pytest import mark
from loginpage import LoginPage
from homepage import HomePage
from _excel_ import headers, data

_headers = headers("smoke", "test_login_positive")
_data = data("smoke", "test_login_positive")

@mark.parametrize(_headers, _data)
def test_login_positive(setup, email, password):
    # Click on Login Link
    hp = HomePage(setup)
    hp.home_click_login()

    # Call POM functions
    lp = LoginPage(setup)
    lp.login_enter_email(email)
    lp.login_enter_password(password)
    lp.login_click_login()

    # Verify the user is logged in to the application
    assert hp.home_is_login_success(email) == True

# ---------------------------------------------------------------------------------------
_headers = headers("smoke", "test_login_negative")
_data = data("smoke", "test_login_negative")

@mark.parametrize(_headers, _data)
def test_login_negative(setup, email, password, error_message):
    # Click on Login Link
    hp = HomePage(setup)
    hp.home_click_login()

    # Call POM functions
    lp = LoginPage(setup)
    lp.login_enter_email(email)
    lp.login_enter_password(password)
    lp.login_click_login()

    # Verify the auth error is displayed or not
    assert lp.is_auth_error_displayed(error_message) == True

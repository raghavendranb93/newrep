from pytest import mark
from loginpage4 import LoginPage
from homepage4 import HomePage
from _excel_ import headers, data

# headers = "email, password"
# data = [
#     ("bill.gates@company.com", "Password123"),
#     ("hello.world@company.com", "Password123")
#     ]

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


# headers = "email, password, error_message"
# data = [
#     ("bill.gates@company.com", "Password12", "Login was unsuccessful. Please correct the errors and try again."),
#     ("hello.world", "Password123", "Please enter a valid email address.")
#     ]

_headers = headers("smoke", "test_login_negative")
_data = data("smoke", "test_login_negative")

@mark.parametrize(headers, data)
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

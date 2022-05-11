from selenium_wrapper import SeleniumWrapper
from pytest import mark
from lib import is_login_success

headers = "email, password"

data = [
    ("bill.gates@company.com", "Password123"),
    ("hello.world@company.com", "Password123")
    ]

@mark.parametrize(headers, data)
def test_login_positive(setup, email, password):
    s = SeleniumWrapper(setup)      # SeleniumWrapper(driver)
    s.click_element(("link text", "Log in"))
    s.enter_text(("id", "Email"), value=email)
    s.enter_text(("id", "Password"), value=password)
    s.click_element(("xpath", "//input[@value='Log in']"))
    if is_login_success(email):
        print("Success")
    else:
        print("FAIL")



# headers = "email, password"
# data = [
#     ("bill.gates@company.com", "Password12", "Login was unsuccessful. Please correct the errors and try again."),
#     ("hello.world", "Password123", "Please enter a valid email address.")
#     ]

# @mark.parametrize(headers, data)
# def test_login_positive(setup, email, password):
#     s = SeleniumWrapper(setup)      # SeleniumWrapper(driver)
#     s.click_element(("link text", "Log in"))
#     s.enter_text(("id", "Email"), value=email)
#     s.enter_text(("id", "Password"), value=password)
#     s.click_element(("xpath", "//input[@value='Log in']"))


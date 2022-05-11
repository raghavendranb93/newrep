from selenium_wrapper import SeleniumWrapper
from pytest import mark
from lib import is_auth_error_displayed

headers = "gender, fname, lname, email, password"

data = [
    ("male", "steve", "jobs", "steve.jobs@comapny.com", "Password123"),
    ("female", "laura", "turner", "laura.turner@comapny.com", "Password123")
]

@mark.parametrize(headers, data)
def test_registration(setup, gender, fname, lname, email, password):
    s = SeleniumWrapper(setup)
    s.click_element(("link text", "Register"))
    if gender == "male":
        s.click_element(("id", "gender-male"))
    elif gender == "female":
        s.click_element(("id", "gender-female"))
    else:
        raise Exception("Unknown Gender")
    s.enter_text(("id", "FirstName"), value=fname)
    s.enter_text(("id", "LastName"), value=lname)
    s.enter_text(("id", "Email"), value=email)
    s.enter_text(("id", "Password"), value=password)
    s.enter_text(("id", "ConfirmPassword"), value=password)
    s.click_element(("id", "register-button"))


from selenium_wrapper import SeleniumWrapper
from homepage import HomePage
from pytest import mark
from _excel_ import headers, data
from registrationpage import RegistrationPage

# headers = "gender, fname, lname, email, password"
#
# data = [
#     ("male", "steve", "jobs", "steve.jobs@comapny.com", "Password123"),
#     ("female", "laura", "turner", "laura.turner@comapny.com", "Password123")
# ]

_headers = headers("smoke", "test_registration")
_data = data("smoke", "test_registration")


@mark.parametrize(_headers, _data)
def test_registration(setup, gender, fname, lname, email, password):
    hp = HomePage(setup)
    hp.home_click_register()
    # s = SeleniumWrapper(setup)
    # s.click_element(("link text", "Register"))
    rp = RegistrationPage(setup)
    if gender == "male":
        rp.reg_select_male()
    elif gender == "female":
        rp.reg_select_female()
    else:
        raise Exception("Unknown Gender")
    rp.reg_enter_fname(fname)
    rp.reg_enter_lname(lname)
    rp.reg_enter_email(email)
    rp.reg_enter_password(password)
    rp.reg_enter_confirm_password(password)
    rp.reg_click_register()

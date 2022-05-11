from selenium_wrapper import SeleniumWrapper
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from _excel_ import locators


class LoginPage(SeleniumWrapper):
    _txt_email = ("id", "Email")
    _txt_password = ("id", "Password")
    _btn_login = ("xpath", "//input[@value='Log in']")

    def __init__(self, driver):
        super().__init__(driver)

    def login_enter_email(self, email):
        self.enter_text(self._txt_email, value=email)

    def login_enter_password(self, password):
        self.enter_text(self._txt_password, value=password)

    def login_click_login(self):
        self.click_element(self._btn_login)

    def is_auth_error_displayed(self, error_messege):
        _xpath = f"//a[text()='{error_messege}']"  # //a[text()='bill.gates@company.com']
        for _ in range(10):
            try:
                result = self.driver.find_element_by_xpath(_xpath).is_displayed()
                if result:
                    return True
                sleep(1)
                continue
            except NoSuchElementException:
                sleep(1)
                continue
        return False
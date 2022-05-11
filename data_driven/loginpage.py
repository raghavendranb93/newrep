from selenium_wrapper import SeleniumWrapper
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from _excel_ import locators

class LoginPage(SeleniumWrapper):
    locators = locators("loginpage")

    def __init__(self, driver):
        super().__init__(driver)

    def login_enter_email(self, email):
        self.enter_text(self.locators['txt_email'], value=email)
    
    def login_enter_password(self, password):
        self.enter_text(self.locators['txt_password'], value=password)
    
    def login_click_login(self):
        self.click_element(self.locators['btn_login'])
    
    def is_auth_error_displayed(self, error_message):
        _xpath = f"//span[text()='{error_message}']"
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
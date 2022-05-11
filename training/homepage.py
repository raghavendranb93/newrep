from selenium_wrapper import SeleniumWrapper
from time import sleep
from selenium.common.exceptions import NoSuchElementException

class HomePage(SeleniumWrapper):
    _lnk_register = ("link text", "Register")
    _lnk_login = ("link text", "Log in")

    def __init__(self, driver):
        super().__init__(driver)
    
    def home_click_register(self):
        self.click_element(self._lnk_register)
    
    def home_click_login(self):
        self.click_element(self._lnk_login)

    def home_is_login_success(self, email):
        """
        Returns True if the user is logged in successfully else returns False
        """
        _xpath = f"//a[text()='{email}']"   # //a[text()='bill.gates@company.com']
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
from time import sleep
from selenium.common.exceptions import NoSuchElementException



def is_login_success(self, email):
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

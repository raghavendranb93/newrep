from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
import csv
import re
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.remote.webelement import WebElement

driver = Chrome(r"C:\Users\RAGHAVENDRA\Desktop\trainee\chromedriver.exe")
driver.get("http://demowebshop.tricentis.com/")

# driver.get(r"C:\Users\RAGHAVENDRA\Desktop\loading.html")

class _visibility_of_element_located(visibility_of_element_located):
    def __call__(self, driver):
        result = super().__call__(driver)
        # checking if __call__ has returned a WebElement?
        if isinstance(result, WebElement):
            print("Checking for Enblement")
            return result.is_enabled()
        return result

def wait(func):
    def wrapper(*args, **kwargs):
        locator = args[0]
        # Wait (3 Conditions)
        wait = WebDriverWait(driver, 10)
        v = _visibility_of_element_located(locator)
        wait.until(v)
        return func(*args, **kwargs)
    return wrapper

@wait      # enter_text = wait(enter_text)
def enter_text(locator, *, value):
    driver.find_element(*locator).send_keys(value)

@wait
def click_element(locator):
    driver.find_element(*locator).click()

@wait
def select_item():
    ...


click_element(('link text', 'Register'))
click_element(('id', 'gender-male'))
enter_text(('id', 'FirstName'), value='hello')
enter_text(('id', 'LastName'), value='world')
enter_text(('name', 'Email'), value='hello.world@company.com')
enter_text(('id', 'Password'), value='Password123')
enter_text(('id', 'ConfirmPassword'), value='Password123')
click_element(('xpath', "//input[@value='Register']"))

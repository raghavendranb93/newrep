from selenium.webdriver import Chrome
from pytest import fixture

@fixture
def setup():
    driver = Chrome("./chromedriver.exe")
    driver.get(r"http://demowebshop.tricentis.com/")
    yield driver
    driver.close()

@fixture
def greet():
    print("Executing before class")
    yield "hello world"
    print("Executing after class")
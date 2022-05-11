from selenium.webdriver import Chrome
from selenium_wrapper import SeleniumWrapper


# def test_resgistration():
#     driver = Chrome("./chromedriver.exe")
#     driver.get(r"http://demowebshop.tricentis.com/")
#
#     s = SeleniumWrapper(driver)
#
#     s.click_element(('link text', 'Register'))
#     s.click_element(('id', 'gender-male'))
#     s.enter_text(('id', 'FirstName'), value='hello')
#     s.enter_text(('id', 'LastName'), value='world')
#     s.enter_text(('name', 'Email'), value='hello.world@company.com')
#     s.enter_text(('id', 'Password'), value='Password123')
#     s.enter_text(('id', 'ConfirmPassword'), value='Password123')
#     s.click_element(('xpath', "//input[@value='Register']"))

# def test_resgistration(setup):
#
#     s = SeleniumWrapper(setup)
#
#     s.click_element(('link text', 'Register'))
#     s.click_element(('id', 'gender-male'))
#     s.enter_text(('id', 'FirstName'), value='hello')
#     s.enter_text(('id', 'LastName'), value='world')
#     s.enter_text(('name', 'Email'), value='hello.world@company.com')
#     s.enter_text(('id', 'Password'), value='Password123')
#     s.enter_text(('id', 'ConfirmPassword'), value='Password123')
#     s.click_element(('xpath', "//input[@value='Register']"))

# class TestSpam:
#     def test_spam(self, greet):
#         print("Executing test_spam")
#         print(greet)
#
#     def test_apple(self):
#         print("Executing test_apple")

class TestDemo:
    def test_demo(self, greet):
        print("Executing test_demo")
        print(greet)

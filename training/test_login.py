from selenium.webdriver import Chrome
from selenium_wrapper import SeleniumWrapper


# def test_login():
#     driver = Chrome("./chromedriver.exe")
#     driver.get(r"http://demowebshop.tricentis.com/")
#
#     s = SeleniumWrapper(driver)
#
#     s.click_element(("xpath", "//a[text()='Log in']"))
#     s.enter_text(("id", "Email"), value="bill.gates@company.com")
#     s.enter_text(("id", "Password"), value="123@bill")
#     s.click_element(("xpath", "//input[@value='Log in']"))

# def test_login(setup):
#
#     s = SeleniumWrapper(setup)
#
#     s.click_element(("xpath", "//a[text()='Log in']"))
#     s.enter_text(("id", "Email"), value="bill.gates@company.com")
#     s.enter_text(("id", "Password"), value="123@bill")
#     s.click_element(("xpath", "//input[@value='Log in']"))


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
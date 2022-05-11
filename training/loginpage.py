from selenium_wrapper import SeleniumWrapper

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
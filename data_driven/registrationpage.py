from selenium_wrapper import SeleniumWrapper
from _excel_ import locators

class RegistrationPage(SeleniumWrapper):
    locators = locators("registrationpage")

    def __init__(self, driver):
        super().__init__(driver)
    
    def reg_select_male(self):
        self.click_element(self.locators['rdo_male'])
    
    def reg_select_female(self):
        self.click_element(self.locators['rdo_female'])
    
    def reg_enter_fname(self, fname):
        self.enter_text(self.locators['txt_fname'], value=fname)
    
    def reg_enter_lname(self, lname):
        self.enter_text(self.locators['txt_lname'], value=lname)
    
    def reg_enter_email(self, email):
        self.enter_text(self.locators['txt_email'], value=email)
    
    def reg_enter_password(self, password):
        self.enter_text(self.locators['txt_password'], value=password)
    
    def reg_enter_confirm_password(self, confirm_password):
        self.enter_text(self.locators['txt_confirm_password'], value=confirm_password)
    
    def reg_click_register(self):
        self.click_element(self.locators['btn_register'])
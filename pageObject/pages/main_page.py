from selenium.webdriver.common.by import By
from pageObject.BaseApp import BaseApp

class MainPageSelector(object):
    emailInput = (By.XPATH, '//input[@data-testid="login-input"]')
    enterPasswordBtn = (By.XPATH, '//button[@data-testid="enter-password"]')
    passwordInput = (By.XPATH, '//input[@data-testid="password-input"]')
    loginBtn = (By.XPATH, '//button[@data-testid="login-to-mail"]')

class MainPage(BaseApp):
    def __init__(self, driver):
        super(MainPage, self).__init__(driver)

    def open_main_page(self):
        self.go_to_site()

    def fill_login(self, login):
        emailInput = self.find_element(MainPageSelector.emailInput)
        emailInput.send_keys(login)
    
    def click_btn_enter_password(self):
        btn = self.find_element(MainPageSelector.enterPasswordBtn)
        btn.click()

    def fill_password(self, password):
        passwordInput = self.find_element(MainPageSelector.passwordInput)
        passwordInput.send_keys(password)

    def click_btn_login(self):
        btn = self.find_element(MainPageSelector.loginBtn)
        btn.click()
        
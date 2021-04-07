from selenium.webdriver.common.by import By
from pageObject.BaseApp import BaseApp


class EmailPageSet(object):
    newEmailBtn = (By.CSS_SELECTOR, 'span.compose-button__wrapper')
    contactsInput = (By.XPATH, '//div[contains(@class, "contactsContainer")]//input')
    bodyEmailDiv = (By.XPATH, '//div[@role="textbox"]/div[1]')
    sendBtn = (By.XPATH, '//span[@data-title-shortcut="Ctrl+Enter"]')


class EmailPage(BaseApp):
    def __init__(self, driver):
        super(EmailPage, self).__init__(driver)

    def click_btn_new_email(self):
        btn = self.find_element(EmailPageSet.newEmailBtn)
        btn.click()

    def fill_contact(self, contact_email):
        contacts_input = self.find_element(EmailPageSet.contactsInput)
        contacts_input.send_keys(contact_email)

    def fill_body_email(self, body_email):
        body_email_div = self.find_element(EmailPageSet.bodyEmailDiv)
        body_email_div.send_keys(body_email)

    def click_btn_send_email(self):
        btn = self.find_element(EmailPageSet.sendBtn)
        btn.click()

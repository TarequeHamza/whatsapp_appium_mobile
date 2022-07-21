import time

from Locators.Locators import WhatsAppLoginLocators
from Pages.HomePage import HomePage


class WhatsAppPage(HomePage):

    def __init__(self, driver: object) -> object:
        self.locator = WhatsAppLoginLocators
        self.driver = driver
        super(WhatsAppPage, self).__init__(driver)

    def click_agreeAndContinue(self):
        self.find_element(*self.locator.agreeAndContinue).click()

    def type_phone_number(self, text):
        self.find_element(*self.locator.phoneNumberTextBox).send_keys(text)

    def click_next_button(self):
        self.find_element(*self.locator.phoneNumberNextButton).click()

    def click_ok_button(self):
        self.find_element(*self.locator.okButton).click()

    def click_continue_button(self):
        self.find_element(*self.locator.continueButton).click()
        time.sleep(10)

    def click_skip_button(self):
        self.find_element(*self.locator.skipButton).click()

    def click_skip_restore_button(self):
        self.find_element(*self.locator.skipRestoreButton).click()

    def click_profile_name_next_button(self):
        self.find_element(*self.locator.profileNameNextButton).click()
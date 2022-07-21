import time

from Locators.Locators import WhatsAppContactSaveLocators
from Pages.HomePage import HomePage


class AvailabilityPage(HomePage):

    def __init__(self, driver: object) -> object:
        self.locator = WhatsAppContactSaveLocators
        self.driver = driver
        super(AvailabilityPage, self).__init__(driver)

    def is_Displayed(self):
        return self.find_element(*self.locator.expectedProfileName).is_displayed()

    def is_Displayed_invite(self):
        return self.find_element(*self.locator.inviteToWhatsApp).is_displayed()

    def get_text_rowStatus(self):
        text = self.find_element(*self.locator.rowStatus).text
        return text

    # def click_search_icon(self):
    #     self.find_element(*self.locator.searchIcon).click()
    #     time.sleep(3)
    #     self.find_element(*self.locator.searchTextBox).click()
    #
    # def type_phone_number(self, number):
    #     self.find_element(*self.locator.searchTextBox).send_keys(number)
    #     time.sleep(3)
    #
    # def click_expected_profile(self):
    #     self.find_element(*self.locator.contactSelect).click()
    #     time.sleep(3)
    #
    # def type_message(self, message):
    #     self.find_element(*self.locator.sendMessageTextBox).send_keys(message)
    #     time.sleep(3)
    #
    # def click_send_button(self):
    #     self.find_element(*self.locator.sendButton).click()
    #     time.sleep(3)
    #
    # def click_back_button(self):
    #     self.find_element(*self.locator.backIcon).click()
    #     time.sleep(3)

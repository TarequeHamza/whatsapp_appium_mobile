import time
from Locators.Locators import WhatsAppContactSaveLocators
from Pages.HomePage import HomePage


class SaveContactPage(HomePage):

    def __init__(self, driver: object) -> object:
        self.locator = WhatsAppContactSaveLocators
        self.driver = driver
        super(SaveContactPage, self).__init__(driver)

    def get_text(self):
        text = self.find_element(*self.locator.expectedProfileName).text
        return text

    def get_text_for_invite(self):
        text = self.find_element(*self.locator.inviteButton).text
        return text

    def click_backArrow_icon(self):
        self.find_element(*self.locator.backArrowIcon).click()
        time.sleep(3)

    def click_new_contact_button(self):
        self.find_element(*self.locator.newContact).click()
        time.sleep(3)

    def type_first_name(self, firstName):
        self.find_element(*self.locator.firstNameTextBox).send_keys(firstName)
        time.sleep(3)

    def type_last_name(self, lastName):
        self.find_element(*self.locator.lastNameTextBox).send_keys(lastName)
        time.sleep(3)

    def type_phone_number(self, number):
        self.find_element(*self.locator.phoneNumberTextBox).send_keys(number)
        time.sleep(3)


    def click_save_button(self):
        self.find_element(*self.locator.saveButtonForNumberSave).click()
        time.sleep(3)


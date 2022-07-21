import time

from Locators.Locators import WhatsAppLoginLocators
from Pages.HomePage import HomePage

class SchedulePage(HomePage):

    def __init__(self, driver: object) -> object:
        self.locator = WhatsAppLoginLocators
        self.driver = driver
        super(SchedulePage, self).__init__(driver)

    def click_schedule(self, *locator):
        self.find_element(*self.locator.click_schedule).click()
        time.sleep(3)
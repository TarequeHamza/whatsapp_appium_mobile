import time

from Pages.BasePage import BasePage
from Pages.WhatsAppPage import WhatsAppPage


class LoginTest(BasePage):

    def test_LoginPage(self):
        login = WhatsAppPage(self.driver)
        login.click_agreeAndContinue()
        time.sleep(3)
        login.type_phone_number("1791859174")
        time.sleep(3)
        login.click_next_button()
        time.sleep(3)
        login.click_ok_button()
        time.sleep(3)
        login.click_continue_button()
        time.sleep(10)
        login.click_skip_button()
        time.sleep(10)
        login.click_skip_restore_button()
        time.sleep(10)
        login.click_profile_name_next_button()
        time.sleep(10)

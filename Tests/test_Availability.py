import time

from Pages.BasePage import BasePage
from Pages.SendMessagePage import SendMessagePage
from Pages.ContactSavePage import SaveContactPage
from Pages.AvailabilityPage import AvailabilityPage
from utils.ExcelHandling import *
import os.path


class SendMessageTest(BasePage):
    def test_SendMessage(self):
        send = SendMessagePage(self.driver)
        save = SaveContactPage(self.driver)
        available = AvailabilityPage(self.driver)
        excel = os.path.abspath('..\TestData\Contract_Number_List.xlsx')
        firstName = open_and_read_excel_file(excel, "Sheet1", 1)
        # lastName = open_and_read_excel_file(excel, "Sheet1", 2)
        number = open_and_read_excel_file(excel, "Sheet1", 3)
        send.click_message_icon()
        for i in range(len(number)):
            send.click_search_icon()
            send.type_phone_number(number[i])
            time.sleep(5)
            Text = f"No results found for '{number[i]}'"
            if Text == save.get_text():

                save.click_backArrow_icon()
                time.sleep(2)
                save.click_new_contact_button()
                time.sleep(3)
                save.type_first_name(firstName[i])
                self.driver.swipe(500, 920, 500, 500, 1000)
                # save.type_last_name(lastName[i])
                save.type_phone_number(number[i])
                save.click_save_button()
                self.driver.back()
                time.sleep(5)
                send.click_search_icon()
                send.type_phone_number(number[i])
                time.sleep(5)


                if len(available.get_text_rowStatus()) == 16:

                    writeData(excel, "Sheet1", i + 2, 4, "0")
                    time.sleep(3)
                    save.click_backArrow_icon()
                    time.sleep(3)


                else:


                    # send.click_expected_profile()
                    # time.sleep(3)
                    # send.type_message("Hi there!\nPut the musk on your face!\nStay safe, stay healthy, keep healthy others!")
                    # send.click_send_button()
                    # time.sleep(3)
                    # send.click_back_button()
                    # time.sleep(2)
                    # send.click_message_icon()
                    # time.sleep(2)
                    writeData(excel, "Sheet1", i + 2, 4, "1")
                    time.sleep(2)


            else:

                if len(available.get_text_rowStatus()) == 16:

                    writeData(excel, "Sheet1", i + 2, 4, "0")
                    time.sleep(3)
                    save.click_backArrow_icon()
                    time.sleep(3)

                else:

                    # send.click_expected_profile()
                    # time.sleep(3)
                    # send.type_message("Hi there!\nPut the musk on your face!\nStay safe, stay healthy, keep healthy others!")
                    # send.click_send_button()
                    # time.sleep(3)
                    # send.click_back_button()
                    # time.sleep(2)
                    # send.click_message_icon()
                    # time.sleep(2)
                    writeData(excel, "Sheet1", i + 2, 4, "1")
                    time.sleep(2)
                    save.click_backArrow_icon()

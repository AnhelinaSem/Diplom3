from locators.password_recovery_locators import PasswordRecoveryLocators
from pages.base_page import BasePage

class PasswordRecoveryPage(BasePage):
    def click_recover_password(self):
        self.wait_for_element_to_be_clickable(PasswordRecoveryLocators.RECOVER_PASSWORD_BUTTON).click()

    def enter_email(self, email):
        email_input = self.wait_for_element_to_be_visible(PasswordRecoveryLocators.EMAIL_INPUT)
        email_input.click()
        email_input.clear()
        email_input.send_keys(email)

    def enter_password(self, password):
        password_input = self.wait_for_element_to_be_visible(PasswordRecoveryLocators.PASSWORD_INPUT)
        password_input.click()
        password_input.clear()
        password_input.send_keys(password)

    def click_submit(self):
        self.wait_for_element_to_be_clickable(PasswordRecoveryLocators.SUBMIT_BUTTON).click()

    def click_show_password(self):
        self.wait_for_element_to_be_clickable(PasswordRecoveryLocators.SHOW_PASSWORD_BUTTON).click()

    def click_hide_password(self):
        self.wait_for_element_to_be_clickable(PasswordRecoveryLocators.HIDE_PASSWORD_BUTTON).click()

    def go_to_password_recovery(self):
        self.wait_for_element_to_be_clickable(PasswordRecoveryLocators.PASSWORD_RECOVERY_LINK).click()

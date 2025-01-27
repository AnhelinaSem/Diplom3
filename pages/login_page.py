from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators

class LoginPage(BasePage):
    def login(self, email, password):
        email_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)
        )
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(LoginPageLocators.EMAIL_INPUT)
        )
        email_input.send_keys(email)
        password_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.PASSWORD_INPUT)
        )
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(LoginPageLocators.PASSWORD_INPUT)
        )
        password_input.send_keys(password)
        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON)
        )
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located((By.CLASS_NAME, "Modal_modal_overlay__x2ZCr"))
        )
        login_button.click()

        WebDriverWait(self.driver, 10).until_not(
            EC.visibility_of_element_located((By.CLASS_NAME, "Modal_modal_overlay__x2ZCr"))
        )

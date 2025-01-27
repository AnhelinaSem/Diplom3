import pytest
from pages.password_recovery_page import PasswordRecoveryPage
from locators.password_recovery_locators import PasswordRecoveryLocators
from data import TestData
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("driver_init")
class TestPasswordRecovery:
    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):
        self.driver.get(TestData.BASE_URL + "login")
        page = PasswordRecoveryPage(self.driver)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@class='Auth_link__1fOlj' and text()='Восстановить пароль']")))
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(By.XPATH, "//a[@class='Auth_link__1fOlj' and text()='Восстановить пароль']"))
        self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.XPATH, "//a[@class='Auth_link__1fOlj' and text()='Восстановить пароль']"))
        yield
        self.driver.delete_all_cookies()

    def close_modal(self):
        try:
            close_modal_button = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "Modal_modal_overlay__x2ZCr"))
            )
            close_modal_button.click()
        except:
            pass

    def test_navigate_to_password_recovery(self):
        page = PasswordRecoveryPage(self.driver)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(PasswordRecoveryLocators.PASSWORD_RECOVERY_HEADER))
        assert self.driver.find_element(*PasswordRecoveryLocators.PASSWORD_RECOVERY_HEADER).is_displayed()

    def test_enter_email_and_submit(self):
        page = PasswordRecoveryPage(self.driver)
        self.close_modal()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(PasswordRecoveryLocators.EMAIL_INPUT))
        page.enter_email(TestData.EMAIL)
        self.close_modal()
        page.click_submit()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(PasswordRecoveryLocators.PASSWORD_INPUT))
        assert self.driver.find_element(*PasswordRecoveryLocators.PASSWORD_INPUT).is_displayed()

    def test_show_hide_password(self):
        page = PasswordRecoveryPage(self.driver)
        self.close_modal()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(PasswordRecoveryLocators.EMAIL_INPUT))
        page.enter_email(TestData.EMAIL)
        self.close_modal()
        page.click_submit()
        self.close_modal()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(PasswordRecoveryLocators.PASSWORD_INPUT))

        self.close_modal()

        page.enter_password(TestData.PASSWORD)
        self.close_modal()
        assert self.driver.find_element(*PasswordRecoveryLocators.PASSWORD_INPUT).get_attribute("type") == "password"

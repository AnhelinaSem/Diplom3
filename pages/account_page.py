from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.personal_account_locators import PersonalAccountLocators


class PersonalAccountPage(BasePage):
    def click_to_element(self, locator):
        WebDriverWait(self.driver, 3).until(
            EC.element_to_be_clickable(locator)
        )
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].click();", element)

    def wait_element_invisibility(self, wait_locator=(By.CLASS_NAME, "Modal_modal_overlay__x2ZCr")):
        element = self.driver.find_element(*wait_locator)
        WebDriverWait(self.driver, 30).until(
            EC.invisibility_of_element_located(element)
        )

    def go_to_personal_account(self):
        self.wait_element_invisibility()
        self.click_to_element(PersonalAccountLocators.PERSONAL_ACCOUNT_BUTTON)

    def go_to_order_history(self):
        self.click_to_element(PersonalAccountLocators.ORDER_HISTORY_SECTION)

    def logout(self):
        self.click_to_element(PersonalAccountLocators.LOGOUT_BUTTON)

    def wait_for_url(self, url_fragment):
        WebDriverWait(self.driver, 10).until(EC.url_contains(url_fragment))
        assert url_fragment in self.driver.current_url

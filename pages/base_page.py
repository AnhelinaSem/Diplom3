from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def wait_for_element_to_be_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def wait_for_element_to_be_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def close_modal(self):
        try:
            close_modal_button = self.wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "Modal_modal__close__TnseK"))
            )
            close_modal_button.click()
        except:
            pass

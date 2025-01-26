from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.order_locators import FeedPageLocators
from selenium.webdriver.common.action_chains import ActionChains
from locators.order_locators import OrderPageLocators


class FeedPage(BasePage):
    def click_order_card(self):
        order_card = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(FeedPageLocators.ORDER_CARD)
        )
        order_card.click()

    def is_order_modal_visible(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(FeedPageLocators.ORDER_MODAL)
            )
            return True
        except:
            return False

    def get_completed_all_time_count(self):
        # Wait for the stats section to load
        total_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p"))
        )
        return int(total_element.text)

    def get_completed_today_count(self):
        total_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p"))
        )
        return int(total_element.text)

    def is_order_in_progress(self, order_number):
        orders_in_progress = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located(FeedPageLocators.ORDERS_IN_PROGRESS)
        )
        for order in orders_in_progress:
            if order.text == order_number:
                return True
        return False



class OrderPage(BasePage):
    def drag_and_drop_ingredient_to_order(self):
        ingredient = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[text()='Флюоресцентная булка R2-D3']"))
        )
        order_area = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(OrderPageLocators.ORDER_SECTION)
        )
        actions = ActionChains(self.driver)
        actions.drag_and_drop(ingredient, order_area).perform()








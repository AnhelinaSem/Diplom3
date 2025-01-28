
from pages.main_page import MainPage

from pages.base_page import BasePage
from locators.order_locators import FeedPageLocators
from locators.order_locators import OrderPageLocators
from locators.main_page_locators import MainPageLocators
from data import TestData
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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

        total_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p"))
        )
        return int(total_element.text)

    def get_completed_today_count(self):
        total_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//p[@class 'text text_type_main-medium' and text()='Выполнено за сегодня:']/following-sibling::p"))
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

    def create_order_and_get_number(self):
        main_page = MainPage(self.driver)


        self.driver.get(TestData.BASE_URL)

        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(MainPageLocators.INGREDIENT)
        )
        main_page.drag_and_drop_ingredient_to_order()

        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Войти в аккаунт']"))
        )
        login_button.click()

        login_page = LoginPage(self.driver)
        login_page.login(TestData.EMAIL, TestData.PASSWORD)

        place_order_button = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Оформить заказ']"))
        )
        place_order_button.click()

        order_number = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "text_type_digits-large"))
        ).text

        try:
            close_button = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK"))
            )
            close_button.click()
        except:
            pass

        return order_number




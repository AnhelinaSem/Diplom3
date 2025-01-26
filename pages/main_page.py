from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.common.action_chains import ActionChains

class MainPage(BasePage):
    def click_constructor(self):
        constructor_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.CONSTRUCTOR_BUTTON)
        )
        constructor_button.click()

    def click_order_feed(self):
        order_feed_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.ORDER_FEED_BUTTON)
        )
        order_feed_button.click()

    def click_ingredient(self):
        ingredient = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.INGREDIENT)
        )
        ingredient.click()

    def close_ingredient_details_popup(self):
        close_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.CLOSE_POPUP_BUTTON)
        )
        close_button.click()

    def get_ingredient_counter(self):
        counter = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(MainPageLocators.INGREDIENT_COUNTER)
        )
        return int(counter.text)

    def drag_and_drop_ingredient_to_order(self):
        ingredient = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.INGREDIENT)
        )
        order_area = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.ORDER_SECTION)
        )
        actions = ActionChains(self.driver)
        actions.drag_and_drop(ingredient, order_area).perform()

    def place_order(self):

        place_order_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.PLACE_ORDER_BUTTON)
        )
        place_order_button.click()


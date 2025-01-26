import pytest
from pages.order_page import FeedPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.order_page import OrderPage
from locators.order_locators import FeedPageLocators
from locators.order_locators import OrderPageLocators
from locators.main_page_locators import MainPageLocators
from data import TestData
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("driver_init")
class TestFeedPage:
    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):

        self.driver.get(TestData.BASE_URL)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "AppHeader_header__logo__2D0X2"))
        )

        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'button_button')]"))
        )
        login_button.click()

        login_page = LoginPage(self.driver)
        login_page.login(TestData.EMAIL, TestData.PASSWORD)

        self.driver.get(TestData.BASE_URL + "feed")

        yield

        self.driver.delete_all_cookies()

    def create_order_and_get_number(self):
        main_page = MainPage(self.driver)
        order_page = OrderPage(self.driver)

        self.driver.get(TestData.BASE_URL)

        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(MainPageLocators.INGREDIENT)
        )
        main_page.drag_and_drop_ingredient_to_order()

        place_order_button = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "button_button__33qZ0"))
        )
        place_order_button.click()

        order_number = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(OrderPageLocators.ORDER_CONFIRMATION)
        ).text
        return order_number

    def test_order_details_modal(self):
        feed_page = FeedPage(self.driver)

        feed_page.click_order_card()
        assert feed_page.is_order_modal_visible()

    def test_orders_displayed_in_feed(self):
        feed_page = FeedPage(self.driver)

        order_cards = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_all_elements_located(FeedPageLocators.ORDER_CARD)
        )
        assert len(order_cards) > 0

    def test_completed_all_time_counter(self):

        self.driver.get(TestData.BASE_URL + "feed")
        feed_page = FeedPage(self.driver)

        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(FeedPageLocators.ORDER_CARD)
        )

        initial_count = feed_page.get_completed_all_time_count()
        self.create_order_and_get_number()

        self.driver.get(TestData.BASE_URL + "feed")
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(FeedPageLocators.ORDER_CARD)
        )

        new_count = feed_page.get_completed_all_time_count()
        assert new_count > initial_count

    def test_completed_today_counter(self):

        self.driver.get(TestData.BASE_URL + "feed")
        feed_page = FeedPage(self.driver)

        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(FeedPageLocators.ORDER_CARD)
        )

        initial_count = feed_page.get_completed_today_count()
        self.create_order_and_get_number()

        self.driver.get(TestData.BASE_URL + "feed")
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(FeedPageLocators.ORDER_CARD)
        )

        new_count = feed_page.get_completed_today_count()
        assert new_count > initial_count

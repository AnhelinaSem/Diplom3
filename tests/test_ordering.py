import pytest
from pages.order_page import FeedPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.order_page import FeedPage
from pages.base_page import BasePage
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
        self.base_page = BasePage(self.driver)

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "AppHeader_header__logo__2D0X2"))
        )

        try:
            close_button = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "Modal_close__3g5UE"))
            )
            close_button.click()
        except:
            pass

        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.button_button__33qZ0"))
        )
        login_button.click()

        login_page = LoginPage(self.driver)
        login_page.login(TestData.EMAIL, TestData.PASSWORD)

        self.driver.get(TestData.BASE_URL + "feed")

        yield

        self.driver.delete_all_cookies()



    def test_order_details_modal(self):
        feed_page = FeedPage(self.driver)
        self.base_page.close_modal()

        feed_page.click_order_card()
        assert feed_page.is_order_modal_visible()

    def test_orders_displayed_in_feed(self):
        feed_page = FeedPage(self.driver)
        self.base_page.close_modal()

        order_cards = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_all_elements_located(FeedPageLocators.ORDER_CARD)
        )
        assert len(order_cards) > 0



    def test_completed_all_time_counter(self):
        self.driver.get(TestData.BASE_URL + "feed")
        feed_page = FeedPage(self.driver)
        self.base_page.close_modal()

        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(FeedPageLocators.ORDER_CARD)
        )

        initial_count = order_page.get_completed_all_time_count()

        self.driver.get(TestData.BASE_URL)
        self.order_page.create_order_and_get_number()

        try:
            close_button = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(OrderPageLocators.MODAL_ORDER)
            )
            close_button.click()
        except:
            pass

        self.driver.get(TestData.BASE_URL + "feed")
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(FeedPageLocators.ORDER_CARD)
        )

        new_count = order_page.get_completed_all_time_count()
        assert new_count > initial_count



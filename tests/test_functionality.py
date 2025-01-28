import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.account_page import PersonalAccountPage
from locators.main_page_locators import MainPageLocators
from locators.order_locators import OrderPageLocators
from locators.login_page_locators import LoginPageLocators
from data import TestData


@pytest.mark.usefixtures("driver_init")
class TestMainFunctionality:
    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):

        self.driver.get(TestData.BASE_URL)
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

    def test_navigate_to_constructor(self):
        page = MainPage(self.driver)
        page.click_constructor()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(MainPageLocators.CONSTRUCTOR_HEADER))
        assert self.driver.find_element(*MainPageLocators.CONSTRUCTOR_HEADER).is_displayed()

    def test_navigate_to_order_feed(self):
        page = MainPage(self.driver)
        self.close_modal()

        page.click_order_feed()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(MainPageLocators.ORDER_FEED_HEADER))
        assert self.driver.find_element(*MainPageLocators.ORDER_FEED_HEADER).is_displayed()

    def test_ingredient_details_popup(self):
        page = MainPage(self.driver)
        self.close_modal()

        page.click_ingredient()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(MainPageLocators.INGREDIENT_DETAILS_POPUP))
        assert self.driver.find_element(*MainPageLocators.INGREDIENT_DETAILS_POPUP).is_displayed()
        page.close_ingredient_details_popup()
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located(MainPageLocators.INGREDIENT_DETAILS_POPUP))
        assert not self.driver.find_element(*MainPageLocators.INGREDIENT_DETAILS_POPUP).is_displayed()

    def test_ingredient_counter_increases(self):
        page = MainPage(self.driver)
        self.close_modal()

        initial_count = page.get_ingredient_counter()
        page.drag_and_drop_ingredient_to_order()
        new_count = page.get_ingredient_counter()
        assert new_count == initial_count + 2

    def test_logged_in_user_can_place_order(self):
        self.driver.get(TestData.BASE_URL)
        main_page = MainPage(self.driver)

        main_page.drag_and_drop_ingredient_to_order()

        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((LoginPageLocators.LOGIN_LOAD_BUTTON))
        )
        login_button.click()

        login_page = LoginPage(self.driver)
        login_page.login(TestData.EMAIL, TestData.PASSWORD)

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((MainPageLocators.PERSONAL_ACCOUNT))
        )

        self.close_modal()

        place_order_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((OrderPageLocators.PLACE_ORDER_BUTTON))
        )
        place_order_button.click()

        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(OrderPageLocators.ORDER_CONFIRMATION))
        assert self.driver.find_element(*OrderPageLocators.ORDER_CONFIRMATION).is_displayed()

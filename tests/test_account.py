import pytest
from pages.account_page import PersonalAccountPage
from pages.login_page import LoginPage
from data import TestData
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("driver_init")
class TestPersonalAccount:
    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):
        yield

        self.driver.delete_all_cookies()

    def test_go_to_personal_account(self):
        self.driver.get(TestData.BASE_URL)
        page = PersonalAccountPage(self.driver)
        page.go_to_personal_account()

        login_page = LoginPage(self.driver)
        login_page.login(TestData.EMAIL, TestData.PASSWORD)

        self.driver.get(TestData.BASE_URL)
        page.go_to_personal_account()


        page.wait_for_url("account/profile")

    def test_go_to_order_history(self):
        self.driver.get(TestData.BASE_URL)
        page = PersonalAccountPage(self.driver)
        page.go_to_personal_account()

        page.go_to_order_history()

        page.wait_for_url("account/order-history")
        assert "account/order-history" in self.driver.current_url

    def test_logout(self):
        self.driver.get(TestData.BASE_URL)
        page = PersonalAccountPage(self.driver)
        page.go_to_personal_account()

        page.logout()

        page.wait_for_url("login")
        assert "Войти" in self.driver.page_source

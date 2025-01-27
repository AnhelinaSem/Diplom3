from selenium.webdriver.common.by import By

class PersonalAccountLocators:
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[@class = 'AppHeader_header__linkText__3q_va ml-2' and text()='Личный Кабинет']")
    ORDER_HISTORY_SECTION = (By.XPATH, "//a[text()='История заказов']")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    PROFILE_SECTION = (By.XPATH, "//a[text()='Профиль']")


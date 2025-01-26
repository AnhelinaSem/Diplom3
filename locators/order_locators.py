from selenium.webdriver.common.by import By

class FeedPageLocators:
    ORDER_CARD = (By.XPATH, "//h2[@class ='text text_type_main-medium mb-2']")
    ORDER_MODAL = (By.XPATH, "//div[@class='Modal_orderBox__1xWdi Modal_modal__contentBox__sCy8X p-10']")
    ORDERS_TOTAL = (
    By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p[@class='text text_type_digits-large']")
    ORDERS_TODAY = (
    By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p[@class='text text_type_digits-large']")
    IN_PROGRESS_SECTION = (By.XPATH, "//div[@class='in_progress_section']")
    ORDER_NUMBER_IN_PROGRESS = (By.XPATH, "//div[@class='in_progress_section']//p")
    ORDERS_IN_PROGRESS = (By.XPATH, "//div[contains(@class, 'orders_in_progress')]//span")
    ORDER_NUMBER = (By.XPATH, "//span[contains(@class, 'order_number')]")






class OrderPageLocators:
    ADD_INGREDIENT_BUTTON = (By.XPATH, "//button[text()='Добавить']")

    ORDER_CONFIRMATION = (By.XPATH, "//div[@class='Modal_modal__contentBox__sCy8X pt-30 pb-30']")
    ORDER_NUMBER = (By.XPATH, "//span[contains(@class, 'order_number')]")



from selenium.webdriver.common.by import By

class MainPageLocators:
    INGREDIENT_ITEM = (By.XPATH, "//div[contains(@class, 'ingredient')]")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    PASSWORD_RECOVERY_LINK = (By.XPATH, "//a[text()='Забыли пароль?']")
    CONSTRUCTOR_HEADER = (By.XPATH, "//h1[text()='Соберите бургер']")
    ORDER_FEED_HEADER = (By.XPATH, "//h1[text()='Лента заказов']")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[@class='AppHeader_header__linkText__3q_va ml-2' and text()='Конструктор']")
    ORDER_FEED_BUTTON = (By.XPATH, "//a[@class='AppHeader_header__link__3D_hX' and @href='/feed']")
    INGREDIENT = (By.XPATH, "//a[@class='BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8']")
    ORDER_SECTION = (By.XPATH, "//section[@class='BurgerConstructor_basket__29Cd7 mt-25 ']")
    INGREDIENT_DETAILS_POPUP = (By.XPATH, "//h2[text()='Детали ингредиента']")
    INGREDIENT_COUNTER = (By.XPATH, "//div[@class='counter_counter__ZNLkj counter_default__28sqi']")
    CLOSE_POPUP_BUTTON = (By.XPATH, "//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']")
    BUN_LOCATOR = (By.XPATH, "/html/body/div/div/main/section[1]/div[2]/ul[1]/a[1]")
    PLACE_ORDER_BUTTON = (By.XPATH, "//button[@class ='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']")
    ENTER_BUTTON =(By.XPATH, "//button[@class ='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']")
    INGREDIENT_IN_CONSTRUCTOR = (By.XPATH, "//ul[contains(@class, 'BurgerConstructor_basket__list__')]//li")

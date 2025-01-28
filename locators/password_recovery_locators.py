from selenium.webdriver.common.by import By

class PasswordRecoveryLocators:
    RECOVER_PASSWORD_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Введите новый пароль']")
    SHOW_PASSWORD_BUTTON = (By.XPATH, "//input[@type='text' and @name='Введите новый пароль']")
    HIDE_PASSWORD_BUTTON = (By.XPATH, "/html/body/div/div/main/div/form/fieldset[1]/div/div/div/svg")
    SUBMIT_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    PASSWORD_RECOVERY_LINK = (By.XPATH, "//a[@class='Auth_link__1fOlj' and text()='Восстановить пароль']")
    PASSWORD_RECOVERY_HEADER = (By.XPATH, "//h2[text()='Восстановление пароля']")
    PASSWORD_LABEL = (By.XPATH, "//label[contains(@class, 'input__placeholder') and text()='Пароль']")
    PASSWORD_LABEL_FOCUSED = (By.XPATH, "//label[contains(@class, 'input__placeholder') and contains(@class, 'focused') and text()='Пароль']")
    PASSWORD_LABEL_FILLED = (By.XPATH, "//label[contains(@class, 'input__placeholder') and contains(@class, 'filled') and text()='Пароль']")
    PASSWORD_LABEL_FILLED_FOCUSED = (By.XPATH, "//label[contains(@class, 'input__placeholder') and contains(@class, 'filled') and contains(@class, 'focused') and text()='Пароль']")

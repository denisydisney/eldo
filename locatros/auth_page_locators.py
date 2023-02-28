from selenium.webdriver.common.by import By


class AuthPageLocators:
    PC_BATTON = (By.XPATH, "//div[contains(text(),'Кабінет')]")
    PHONE_AUTH = (By.XPATH, "//input[@placeholder='380']")
    SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']")
    PASWORD_AUTH = (By.XPATH, "//input[@placeholder='Введіть пароль для входу']")
    SHOW_PASWORD = (By.XPATH, "//label[@for='showPassword']")
    PC_PAGE = (By.XPATH, "//div[@class='contacts-container bottom-tier']")
    ERROR_TEXT = (By.XPATH, "//span[@class='new-not-require-input-error-text']")
    RECAPTCHA = (By.XPATH, "//iframe[@title='reCAPTCHA']")

    REG_FIRST_NAME = (By.XPATH, "//span[contains(text(),'Ім')]")
    REG_LAST_NAME = (By.XPATH, "//span[contains(text(),'Прізвище')]")
    REG_EMAIL = (By.XPATH, "//span[contains(text(),'Пошта')]")
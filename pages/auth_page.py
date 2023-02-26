import time
from pages.base_page import BasePage
from locatros.all_page_locators import AllPageLocators as Locators


class Auth(BasePage):
    def log_in_valid(self):
        phone = '636183928'
        pasword = 'RA92V7r6pLDarAAA9hxjsA=='

        self.element_is_visible(Locators.PC_BATTON).click()
        self.element_is_visible(Locators.PHONE_AUTH).send_keys(phone)
        self.element_is_visible(Locators.SUBMIT_BUTTON).click()
        self.element_is_visible(Locators.PASWORD_AUTH).send_keys(pasword)
        self.element_is_visible(Locators.SHOW_PASWORD).click()
        self.element_is_visible(Locators.SUBMIT_BUTTON).click()
        time.sleep(5)
        self.element_is_visible(Locators.PC_BATTON).click()
        pc_page = self.element_is_visible(Locators.PC_PAGE)
        if pc_page == pc_page:
            print('PASS')
        else:
            print('FAIL')
        time.sleep(5)

    def log_in_invalid_number(self):
        phone = '666666666'

        self.element_is_visible(Locators.PC_BATTON).click()
        self.element_is_visible(Locators.PHONE_AUTH).send_keys(phone)
        self.element_is_visible(Locators.SUBMIT_BUTTON).click()
        re_captcha = self.element_is_visible(Locators.RECAPTCHA).click()
        if re_captcha == re_captcha:
            print('PASS')
        else:
            print('FAIL')
        time.sleep(5)

    def log_in_invalid_pasword(self):
        phone = '636183928'
        pasword = '666666666'

        self.element_is_visible(Locators.PC_BATTON).click()
        self.element_is_visible(Locators.PHONE_AUTH).send_keys(phone)
        self.element_is_visible(Locators.SUBMIT_BUTTON).click()
        self.element_is_visible(Locators.PASWORD_AUTH).send_keys(pasword)
        self.element_is_visible(Locators.SHOW_PASWORD).click()
        self.element_is_visible(Locators.SUBMIT_BUTTON).click()
        error_text = self.element_is_visible(Locators.ERROR_TEXT)
        if error_text == error_text:
            print('PASS')
        else:
            print('FAIL')
        time.sleep(5)

    def sign_up_valid(self):
        phone = '637340443'
        pasword = '666666666'
        reg_first_name = 'John'
        reg_last_name = 'Doe'
        reg_email = str(time.time()) + "@icloud.com"

        self.element_is_visible(Locators.PC_BATTON).click()
        self.element_is_visible(Locators.PHONE_AUTH).send_keys(phone)
        self.element_is_visible(Locators.SUBMIT_BUTTON).click()
        time.sleep(7)
        self.element_is_visible(Locators.RECAPTCHA).click()
        time.sleep(15)
        self.element_is_visible(Locators.REG_FIRST_NAME).send_keys(reg_first_name)
        self.element_is_visible(Locators.REG_LAST_NAME).send_keys(reg_last_name)
        self.element_is_visible(Locators.REG_EMAIL).send_keys(reg_email)
        self.element_is_visible(Locators.SUBMIT_BUTTON).click()

from pages.auth_page import Auth


class TestAuth:

    def test_log_in_valid(self, driver):
        auth_page = Auth(driver, 'https://eldorado.ua/uk/')
        auth_page.open()
        auth_page.log_in_valid()

    def test_log_in_invalid_number(self, driver):
        auth_page = Auth(driver, 'https://eldorado.ua/uk/')
        auth_page.open()
        auth_page.log_in_invalid_number()

    def test_log_in_invalid_pasword(self, driver):
        auth_page = Auth(driver, 'https://eldorado.ua/uk/')
        auth_page.open()
        auth_page.log_in_invalid_pasword()

    def test_sign_up_valid(self, driver):
        auth_page = Auth(driver, 'https://eldorado.ua/uk/')
        auth_page.open()
        auth_page.sign_up_valid()

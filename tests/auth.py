from pages.order_page import Auth


class TestAuth:

    def test_log_in_valid(self, driver):
        order_page = Auth(driver, 'https://eldorado.ua/uk/')
        order_page.open()
        order_page.log_in_valid()

    def test_log_in_invalid_number(self, driver):
        order_page = Auth(driver, 'https://eldorado.ua/uk/')
        order_page.open()
        order_page.log_in_invalid_number()

    def test_log_in_invalid_pasword(self, driver):
        order_page = Auth(driver, 'https://eldorado.ua/uk/')
        order_page.open()
        order_page.log_in_invalid_pasword()

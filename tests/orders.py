from pages.order_page import FromPage
import pyautogui


class TestFormPage:

    def test_do_pick_up_from_store(self, driver):
        order_page = FromPage(driver, 'https://eldorado.ua/uk/')
        order_page.open()
        pyautogui.scroll(-20)
        order_page.do_pick_up_from_store()

    def test_do_targeted_delivery(self, driver):
        order_page = FromPage(driver, 'https://eldorado.ua/uk/')
        order_page.open()
        pyautogui.scroll(-20)
        order_page.do_targeted_delivery()

    def test_do_new_post_office(self, driver):
        order_page = FromPage(driver, 'https://eldorado.ua/uk/')
        order_page.open()
        pyautogui.scroll(-20)
        order_page.do_new_post_office()

    def test_do_new_post_office_xyn(self, driver):
        order_page = FromPage(driver, 'https://eldorado.ua/uk/')
        order_page.open()
        pyautogui.scroll(-20)
        order_page.do_new_post_office_xyn()
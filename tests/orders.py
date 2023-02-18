from pages.form_page import FromPage
import pyautogui

class TestFormPage:

    def test_do_pick_up_from_store(self, driver):
        form_page = FromPage(driver, 'https://eldorado.ua/uk/')
        form_page.open()
        pyautogui.scroll(-20)
        form_page.do_pick_up_from_store()


    def test_do_targeted_delivery(self, driver):
        form_page = FromPage(driver, 'https://eldorado.ua/uk/')
        form_page.open()
        pyautogui.scroll(-20)
        form_page.do_targeted_delivery()


    def test_do_new_post_office(self, driver):
        form_page = FromPage(driver, 'https://eldorado.ua/uk/')
        form_page.open()
        pyautogui.scroll(-20)
        form_page.do_new_post_office()
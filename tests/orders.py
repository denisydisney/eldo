from pages.order_page import FromPage
import pyautogui
from locatros.form_page_locators import FormPageLocators as Locators


class TestFormPage:

    def test_pick_up_cash(self, driver):
        order_page = FromPage(driver, 'https://eldorado.ua/uk/')
        order_page.open()
        pyautogui.scroll(-20)
        order_page.pick_up_cash()

    def test_pick_up_googlepay(self, driver):
        order_page = FromPage(driver, 'https://eldorado.ua/uk/')
        order_page.open()
        pyautogui.scroll(-20)
        order_page.pick_up_googlepay()

    def test_pick_up_anycard(self, driver):
        order_page = FromPage(driver, 'https://eldorado.ua/uk/')
        order_page.open()
        pyautogui.scroll(-20)
        order_page.pick_up_anycards()

    def test_pick_up_part_super(self, driver):
        order_page = FromPage(driver, 'https://eldorado.ua/uk/')
        order_page.open()
        pyautogui.scroll(-20)
        order_page.pick_up_part_super()

    def test_pick_up_part_privat(self, driver):
        order_page = FromPage(driver, 'https://eldorado.ua/uk/')
        order_page.open()
        pyautogui.scroll(-20)
        order_page.pick_up_part_privat()

    def test_pick_up_part_mono(self, driver):
        order_page = FromPage(driver, 'https://eldorado.ua/uk/')
        pyautogui.scroll(-20)
        order_page.pick_up_part_mono()

    def test_pick_up_part_oschad(self, driver):
        order_page = FromPage(driver, 'https://eldorado.ua/uk/')
        order_page.open()
        pyautogui.scroll(-20)
        order_page.pick_up_part_oschad()

    def test_pick_up_part_abank(self, driver):
        order_page = FromPage(driver, 'https://eldorado.ua/uk/')
        order_page.open()
        pyautogui.scroll(-20)
        order_page.pick_up_part_abank()

    def test_pick_up_part_pumb(self, driver):
        order_page = FromPage(driver, 'https://eldorado.ua/uk/')
        order_page.open()
        pyautogui.scroll(-20)
        order_page.pick_up_part_punb()

    def test_pick_up_part_globus(self, driver):
        order_page = FromPage(driver, 'https://eldorado.ua/uk/')
        order_page.open()
        pyautogui.scroll(-20)
        order_page.pick_up_part_globus()

    def test_pick_up_part_otp(self, driver):
        order_page = FromPage(driver, 'https://eldorado.ua/uk/')
        order_page.open()
        pyautogui.scroll(-20)
        order_page.pick_up_part_otp()

    def test_pick_up_part_sport(self, driver):
        order_page = FromPage(driver, 'https://eldorado.ua/uk/')
        order_page.open()
        pyautogui.scroll(-20)
        order_page.pick_up_part_sport()

    def test_pick_up_part_sense(self, driver):
        order_page = FromPage(driver, 'https://eldorado.ua/uk/')
        order_page.open()
        pyautogui.scroll(-20)
        order_page.pick_up_part_sense()

    #################################################################
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
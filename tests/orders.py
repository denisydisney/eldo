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

    ####################################################################################################################
    def test_targeted_cash(self, driver):
        order_page = FromPage(driver, 'https://eldorado.ua/uk/')
        order_page.open()
        pyautogui.scroll(-20)
        order_page.targeted_cash()

    def test_targeted_privat24(self, driver):
        order_page = FromPage(driver, 'https://eldorado.ua/uk/')
        order_page.open()
        pyautogui.scroll(-20)
        order_page.targeted_privar24()

    def test_targeted_googlepay(self, driver):
        order_page = FromPage(driver, 'https://eldorado.ua/uk/')
        order_page.open()
        pyautogui.scroll(-20)
        order_page.targeted_googlepay()

    def test_targeted_anycard(self, driver):
        order_page = FromPage(driver, 'https://eldorado.ua/uk/')
        order_page.open()
        pyautogui.scroll(-20)
        order_page.targeted_anycard()

    def test_targeted_part_super(self, driver):
        order_page = FromPage(driver, 'https://eldorado.ua/uk/')
        order_page.open()
        pyautogui.scroll(-20)
        order_page.targeted_part_super()

    def test_targeted_part_privat(self, driver):
        order_page = FromPage(driver, 'https://eldorado.ua/uk/')
        order_page.open()
        pyautogui.scroll(-20)
        order_page.targeted_part_privat()

    def test_targeted_part_mono(self, driver):
        order_page = FromPage(driver, 'https://eldorado.ua/uk/')
        order_page.open()
        pyautogui.scroll(-20)
        order_page.targeted_part_mono()

    def test_targeted_part_oschad(self, driver):
        order_page = FromPage(driver, 'https://eldorado.ua/uk/')
        order_page.open()
        pyautogui.scroll(-20)
        order_page.targeted_part_oschad()

    def test_targeted_part_abank(self, driver):
        order_page = FromPage(driver, 'https://eldorado.ua/uk/')
        order_page.open()
        pyautogui.scroll(-20)
        order_page.targeted_part_abank()

    def test_targeted_part_pumb(self, driver):
        order_page = FromPage(driver, 'https://eldorado.ua/uk/')
        order_page.open()
        pyautogui.scroll(-20)
        order_page.targeted_part_pumb()

    def test_targeted_part_globus(self, driver):
        order_page = FromPage(driver, 'https://eldorado.ua/uk/')
        order_page.open()
        pyautogui.scroll(-20)
        order_page.targeted_part_globus()

    def test_targeted_part_otp(self, driver):
        order_page = FromPage(driver, 'https://eldorado.ua/uk/')
        order_page.open()
        pyautogui.scroll(-20)
        order_page.targeted_part_otp()

    def test_targeted_part_sport(self, driver):
        order_page = FromPage(driver, 'https://eldorado.ua/uk/')
        order_page.open()
        pyautogui.scroll(-20)
        order_page.targeted_part_sport()

    def test_targeted_sense(self, driver):
        order_page = FromPage(driver, 'https://eldorado.ua/uk/')
        order_page.open()
        pyautogui.scroll(-20)
        order_page.targeted_part_sense()

    ####################################################################################################################
    def test_new_post_cash(self, driver):
        order_page = FromPage(driver, 'https://eldorado.ua/uk/')
        order_page.open()
        pyautogui.scroll(-20)
        order_page.new_post_cash()

    def test_new_post_privat24(self, driver):
        order_page = FromPage(driver, 'https://eldorado.ua/uk/')
        order_page.open()
        pyautogui.scroll(-20)
        order_page.new_post_privat24()

    def test_new_post_googlepay(self, driver):
        order_page = FromPage(driver, 'https://eldorado.ua/uk/')
        order_page.open()
        pyautogui.scroll(-20)
        order_page.new_post_googlepay()

    def test_new_post_anycard(self, driver):
        order_page = FromPage(driver, 'https://eldorado.ua/uk/')
        order_page.open()
        pyautogui.scroll(-20)
        order_page.new_post_anycards()

    def test_new_post_part_super(self, driver):
        order_page = FromPage(driver, 'https://eldorado.ua/uk/')
        order_page.open()
        pyautogui.scroll(-20)
        order_page.new_post_part_super()

    def test_new_post_part_privat(self, driver):
        order_page = FromPage(driver, 'https://eldorado.ua/uk/')
        order_page.open()
        pyautogui.scroll(-20)
        order_page.new_post_part_privat()

    def test_new_post_part_mono(self, driver):
        order_page = FromPage(driver, 'https://eldorado.ua/uk/')
        order_page.open()
        pyautogui.scroll(-20)
        order_page.new_post_part_mono()

    def test_new_post_part_oschad(self, driver):
        order_page = FromPage(driver, 'https://eldorado.ua/uk/')
        order_page.open()
        pyautogui.scroll(-20)
        order_page.new_post_part_oschad()

    def test_new_post_part_abank(self, driver):
        order_page = FromPage(driver, 'https://eldorado.ua/uk/')
        order_page.open()
        pyautogui.scroll(-20)
        order_page.new_post_part_abank()

    def test_new_post_part_pumb(self, driver):
        order_page = FromPage(driver, 'https://eldorado.ua/uk/')
        order_page.open()
        pyautogui.scroll(-20)
        order_page.new_post_part_punb()

    def test_new_post_part_globus(self, driver):
        order_page = FromPage(driver, 'https://eldorado.ua/uk/')
        order_page.open()
        pyautogui.scroll(-20)
        order_page.new_post_part_globus()

    def test_new_post_part_otp(self, driver):
        order_page = FromPage(driver, 'https://eldorado.ua/uk/')
        order_page.open()
        pyautogui.scroll(-20)
        order_page.new_post_part_otp()

    def test_new_post_part_sport(self, driver):
        order_page = FromPage(driver, 'https://eldorado.ua/uk/')
        order_page.open()
        pyautogui.scroll(-20)
        order_page.new_post_part_sport()

    def test_new_post_sense(self, driver):
        order_page = FromPage(driver, 'https://eldorado.ua/uk/')
        order_page.open()
        pyautogui.scroll(-20)
        order_page.new_post_part_sense()

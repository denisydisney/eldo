import time

from pages.base_page import BasePage
from locatros.form_page_locators import FormPageLocators as Locators


class FromPage(BasePage):
    def pick_up_cash(self):
        phone = '666666666'
        first_name = 'Denys'
        comments = 'Test QA'

        self.element_is_visible(Locators.PRODUCT_CARD).click()
        self.element_is_visible(Locators.BUY_ON_STORE_BUTTON).click()
        self.element_is_visible(Locators.CART).click()
        self.element_is_visible(Locators.CHOOSE_PICK_UP_FROM_STORE).click()
        self.element_is_visible(Locators.CHOOSE_STORE_PICK_UP).click()
        self.element_is_visible(Locators.CHOOSE_PAYMENT_CASH).click()
        self.element_is_visible(Locators.PHONE).send_keys(phone)
        self.element_is_visible(Locators.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(Locators.COMMENTS).send_keys(comments)
        self.element_is_visible(Locators.DONT_CALL).click()
        # self.element_is_visible(Locators.CHECKOUT).click()
        time.sleep(5)

    def pick_up_googlepay(self):
        phone = '666666666'
        first_name = 'Denys'
        second_name = 'Budkov'
        third_name = 'Vasylevych'
        comments = 'Test QA'

        self.element_is_visible(Locators.PRODUCT_CARD).click()
        self.element_is_visible(Locators.BUY_ON_STORE_BUTTON).click()
        self.element_is_visible(Locators.CART).click()
        self.element_is_visible(Locators.CHOOSE_PICK_UP_FROM_STORE).click()
        self.element_is_visible(Locators.CHOOSE_STORE_PICK_UP).click()
        self.element_is_visible(Locators.CHOOSE_PAYMENT_GOOGLEPAY).click()
        self.element_is_visible(Locators.PHONE).send_keys(phone)
        self.element_is_visible(Locators.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(Locators.SECOND_NAME).send_keys(second_name)
        self.element_is_visible(Locators.THIRD_NAME).send_keys(third_name)
        self.element_is_visible(Locators.COMMENTS).send_keys(comments)
        self.element_is_visible(Locators.DONT_CALL).click()
        # self.element_is_visible(Locators.CHECKOUT).click()
        time.sleep(5)

    def pick_up_anycards(self):
        phone = '666666666'
        first_name = 'Denys'
        second_name = 'Budkov'
        third_name = 'Vasylevych'
        comments = 'Test QA'

        self.element_is_visible(Locators.PRODUCT_CARD).click()
        self.element_is_visible(Locators.BUY_ON_STORE_BUTTON).click()
        self.element_is_visible(Locators.CART).click()
        self.element_is_visible(Locators.CHOOSE_PICK_UP_FROM_STORE).click()
        self.element_is_visible(Locators.CHOOSE_STORE_PICK_UP).click()
        self.element_is_visible(Locators.CHOOSE_PAYMENT_ANY_CARDS).click()
        self.element_is_visible(Locators.PHONE).send_keys(phone)
        self.element_is_visible(Locators.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(Locators.SECOND_NAME).send_keys(second_name)
        self.element_is_visible(Locators.THIRD_NAME).send_keys(third_name)
        self.element_is_visible(Locators.COMMENTS).send_keys(comments)
        self.element_is_visible(Locators.DONT_CALL).click()
        # self.element_is_visible(Locators.CHECKOUT).click()
        time.sleep(5)

    def pick_up_part_super(self):
        ipn = '6666666666'
        phone = '666666666'
        first_name = 'Denys'
        second_name = 'Budkov'
        third_name = 'Vasylevych'
        comments = 'Test QA'

        self.element_is_visible(Locators.PRODUCT_CARD).click()
        self.element_is_visible(Locators.BUY_ON_STORE_BUTTON).click()
        self.element_is_visible(Locators.CART).click()
        self.element_is_visible(Locators.CHOOSE_PICK_UP_FROM_STORE).click()
        self.element_is_visible(Locators.CHOOSE_STORE_PICK_UP).click()
        self.element_is_visible(Locators.CHOOSE_PAYMENT_PART).click()
        self.element_is_visible(Locators.CHOOSE_PART_SUPER).click()
        self.element_is_visible(Locators.INPN).send_keys(ipn)
        self.element_is_visible(Locators.PHONE).send_keys(phone)
        self.element_is_visible(Locators.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(Locators.SECOND_NAME).send_keys(second_name)
        self.element_is_visible(Locators.THIRD_NAME).send_keys(third_name)
        self.element_is_visible(Locators.COMMENTS).send_keys(comments)
        self.element_is_visible(Locators.DONT_CALL).click()
        # self.element_is_visible(Locators.CHECKOUT).click()
        time.sleep(5)

    def pick_up_part_mono(self):
        phone = '666666666'
        first_name = 'Denys'
        second_name = 'Budkov'
        third_name = 'Vasylevych'
        comments = 'Test QA'

        self.element_is_visible(Locators.PRODUCT_CARD).click()
        self.element_is_visible(Locators.BUY_ON_STORE_BUTTON).click()
        self.element_is_visible(Locators.CART).click()
        self.element_is_visible(Locators.CHOOSE_PICK_UP_FROM_STORE).click()
        self.element_is_visible(Locators.CHOOSE_STORE_PICK_UP).click()
        self.element_is_visible(Locators.CHOOSE_PAYMENT_PART).click()
        self.element_is_visible(Locators.CHOOSE_PART_MONO).click()
        self.element_is_visible(Locators.PHONE).send_keys(phone)
        self.element_is_visible(Locators.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(Locators.SECOND_NAME).send_keys(second_name)
        self.element_is_visible(Locators.THIRD_NAME).send_keys(third_name)
        self.element_is_visible(Locators.COMMENTS).send_keys(comments)
        self.element_is_visible(Locators.DONT_CALL).click()
        # self.element_is_visible(Locators.CHECKOUT).click()
        time.sleep(5)

    def pick_up_part_oschad(self):
        phone = '666666666'
        first_name = 'Denys'
        second_name = 'Budkov'
        third_name = 'Vasylevych'
        comments = 'Test QA'

        self.element_is_visible(Locators.PRODUCT_CARD).click()
        self.element_is_visible(Locators.BUY_ON_STORE_BUTTON).click()
        self.element_is_visible(Locators.CART).click()
        self.element_is_visible(Locators.CHOOSE_PICK_UP_FROM_STORE).click()
        self.element_is_visible(Locators.CHOOSE_STORE_PICK_UP).click()
        self.element_is_visible(Locators.CHOOSE_PAYMENT_PART).click()
        self.element_is_visible(Locators.CHOOSE_PART_OSCHAD).click()
        self.element_is_visible(Locators.PHONE).send_keys(phone)
        self.element_is_visible(Locators.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(Locators.SECOND_NAME).send_keys(second_name)
        self.element_is_visible(Locators.THIRD_NAME).send_keys(third_name)
        self.element_is_visible(Locators.COMMENTS).send_keys(comments)
        self.element_is_visible(Locators.DONT_CALL).click()
        # self.element_is_visible(Locators.CHECKOUT).click()
        time.sleep(5)

    def pick_up_part_abank(self):
        phone = '666666666'
        first_name = 'Denys'
        second_name = 'Budkov'
        third_name = 'Vasylevych'
        comments = 'Test QA'

        self.element_is_visible(Locators.PRODUCT_CARD).click()
        self.element_is_visible(Locators.BUY_ON_STORE_BUTTON).click()
        self.element_is_visible(Locators.CART).click()
        self.element_is_visible(Locators.CHOOSE_PICK_UP_FROM_STORE).click()
        self.element_is_visible(Locators.CHOOSE_STORE_PICK_UP).click()
        self.element_is_visible(Locators.CHOOSE_PAYMENT_PART).click()
        self.element_is_visible(Locators.CHOOSE_PART_ABANK).click()
        self.element_is_visible(Locators.PHONE).send_keys(phone)
        self.element_is_visible(Locators.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(Locators.SECOND_NAME).send_keys(second_name)
        self.element_is_visible(Locators.THIRD_NAME).send_keys(third_name)
        self.element_is_visible(Locators.COMMENTS).send_keys(comments)
        self.element_is_visible(Locators.DONT_CALL).click()
        # self.element_is_visible(Locators.CHECKOUT).click()
        time.sleep(5)

    def pick_up_part_punb(self):
        phone = '666666666'
        first_name = 'Denys'
        second_name = 'Budkov'
        third_name = 'Vasylevych'
        comments = 'Test QA'

        self.element_is_visible(Locators.PRODUCT_CARD).click()
        self.element_is_visible(Locators.BUY_ON_STORE_BUTTON).click()
        self.element_is_visible(Locators.CART).click()
        self.element_is_visible(Locators.CHOOSE_PICK_UP_FROM_STORE).click()
        self.element_is_visible(Locators.CHOOSE_STORE_PICK_UP).click()
        self.element_is_visible(Locators.CHOOSE_PAYMENT_PART).click()
        self.element_is_visible(Locators.CHOOSE_PART_PUMB).click()
        self.element_is_visible(Locators.PHONE).send_keys(phone)
        self.element_is_visible(Locators.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(Locators.SECOND_NAME).send_keys(second_name)
        self.element_is_visible(Locators.THIRD_NAME).send_keys(third_name)
        self.element_is_visible(Locators.COMMENTS).send_keys(comments)
        self.element_is_visible(Locators.DONT_CALL).click()
        # self.element_is_visible(Locators.CHECKOUT).click()
        time.sleep(5)

    def pick_up_part_globus(self):
        phone = '666666666'
        first_name = 'Denys'
        second_name = 'Budkov'
        third_name = 'Vasylevych'
        comments = 'Test QA'

        self.element_is_visible(Locators.PRODUCT_CARD).click()
        self.element_is_visible(Locators.BUY_ON_STORE_BUTTON).click()
        self.element_is_visible(Locators.CART).click()
        self.element_is_visible(Locators.CHOOSE_PICK_UP_FROM_STORE).click()
        self.element_is_visible(Locators.CHOOSE_STORE_PICK_UP).click()
        self.element_is_visible(Locators.CHOOSE_PAYMENT_PART).click()
        self.element_is_visible(Locators.CHOOSE_PART_GLOBUS).click()
        self.element_is_visible(Locators.PHONE).send_keys(phone)
        self.element_is_visible(Locators.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(Locators.SECOND_NAME).send_keys(second_name)
        self.element_is_visible(Locators.THIRD_NAME).send_keys(third_name)
        self.element_is_visible(Locators.COMMENTS).send_keys(comments)
        self.element_is_visible(Locators.DONT_CALL).click()
        # self.element_is_visible(Locators.CHECKOUT).click()
        time.sleep(5)

    def pick_up_part_otp(self):
        phone = '666666666'
        first_name = 'Denys'
        second_name = 'Budkov'
        third_name = 'Vasylevych'
        comments = 'Test QA'

        self.element_is_visible(Locators.PRODUCT_CARD).click()
        self.element_is_visible(Locators.BUY_ON_STORE_BUTTON).click()
        self.element_is_visible(Locators.CART).click()
        self.element_is_visible(Locators.CHOOSE_PICK_UP_FROM_STORE).click()
        self.element_is_visible(Locators.CHOOSE_STORE_PICK_UP).click()
        self.element_is_visible(Locators.CHOOSE_PAYMENT_PART).click()
        self.element_is_visible(Locators.CHOOSE_PART_OTP).click()
        self.element_is_visible(Locators.PHONE).send_keys(phone)
        self.element_is_visible(Locators.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(Locators.SECOND_NAME).send_keys(second_name)
        self.element_is_visible(Locators.THIRD_NAME).send_keys(third_name)
        self.element_is_visible(Locators.COMMENTS).send_keys(comments)
        self.element_is_visible(Locators.DONT_CALL).click()
        # self.element_is_visible(Locators.CHECKOUT).click()
        time.sleep(5)

    def pick_up_part_sport(self):
        phone = '666666666'
        first_name = 'Denys'
        second_name = 'Budkov'
        third_name = 'Vasylevych'
        comments = 'Test QA'

        self.element_is_visible(Locators.PRODUCT_CARD).click()
        self.element_is_visible(Locators.BUY_ON_STORE_BUTTON).click()
        self.element_is_visible(Locators.CART).click()
        self.element_is_visible(Locators.CHOOSE_PICK_UP_FROM_STORE).click()
        self.element_is_visible(Locators.CHOOSE_STORE_PICK_UP).click()
        self.element_is_visible(Locators.CHOOSE_PAYMENT_PART).click()
        self.element_is_visible(Locators.CHOOSE_PART_SPORT).click()
        self.element_is_visible(Locators.PHONE).send_keys(phone)
        self.element_is_visible(Locators.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(Locators.SECOND_NAME).send_keys(second_name)
        self.element_is_visible(Locators.THIRD_NAME).send_keys(third_name)
        self.element_is_visible(Locators.COMMENTS).send_keys(comments)
        self.element_is_visible(Locators.DONT_CALL).click()
        # self.element_is_visible(Locators.CHECKOUT).click()
        time.sleep(5)

    def pick_up_part_sense(self):
        num_card = '6666'
        phone = '666666666'
        first_name = 'Denys'
        second_name = 'Budkov'
        third_name = 'Vasylevych'
        comments = 'Test QA'

        self.element_is_visible(Locators.PRODUCT_CARD).click()
        self.element_is_visible(Locators.BUY_ON_STORE_BUTTON).click()
        self.element_is_visible(Locators.CART).click()
        self.element_is_visible(Locators.CHOOSE_PICK_UP_FROM_STORE).click()
        self.element_is_visible(Locators.CHOOSE_STORE_PICK_UP).click()
        self.element_is_visible(Locators.CHOOSE_PAYMENT_PART).click()
        self.element_is_visible(Locators.CHOOSE_PART_SENSE).click()
        self.element_is_visible(Locators.NUM_CARD).send_keys(num_card)
        self.element_is_visible(Locators.PHONE).send_keys(phone)
        self.element_is_visible(Locators.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(Locators.SECOND_NAME).send_keys(second_name)
        self.element_is_visible(Locators.THIRD_NAME).send_keys(third_name)
        self.element_is_visible(Locators.COMMENTS).send_keys(comments)
        self.element_is_visible(Locators.DONT_CALL).click()
        # self.element_is_visible(Locators.CHECKOUT).click()
        time.sleep(5)

    def pick_up_part_privat(self):
        phone = '666666666'
        first_name = 'Denys'
        second_name = 'Budkov'
        third_name = 'Vasylevych'
        comments = 'Test QA'

        self.element_is_visible(Locators.PRODUCT_CARD).click()
        self.element_is_visible(Locators.BUY_ON_STORE_BUTTON).click()
        self.element_is_visible(Locators.CART).click()
        self.element_is_visible(Locators.CHOOSE_PICK_UP_FROM_STORE).click()
        self.element_is_visible(Locators.CHOOSE_STORE_PICK_UP).click()
        self.element_is_visible(Locators.CHOOSE_PAYMENT_PART).click()
        self.element_is_visible(Locators.CHOOSE_PART_PRIVAT).click()
        self.element_is_visible(Locators.PHONE).send_keys(phone)
        self.element_is_visible(Locators.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(Locators.SECOND_NAME).send_keys(second_name)
        self.element_is_visible(Locators.THIRD_NAME).send_keys(third_name)
        self.element_is_visible(Locators.COMMENTS).send_keys(comments)
        self.element_is_visible(Locators.DONT_CALL).click()
        # self.element_is_visible(Locators.CHECKOUT).click()
        time.sleep(5)

    def do_targeted_delivery(self):
        street = 'Кіото'
        house = '13'
        flat = '80'
        flor = '11'
        phone = '666666666'
        first_name = 'Denys'
        second_name = 'Budkov'
        third_name = 'Vasylevych'
        comments = 'Test QA'

        self.element_is_visible(Locators.PRODUCT_CARD).click()
        self.element_is_visible(Locators.BUY_ON_STORE_BUTTON).click()
        self.element_is_visible(Locators.CART).click()
        self.element_is_visible(Locators.CHOOSE_TARGETED_DELIVERY).click()
        self.element_is_visible(Locators.STREET).send_keys(street)
        self.element_is_visible(Locators.HOUSE).send_keys(house)
        self.element_is_visible(Locators.FLAT).send_keys(flat)
        self.element_is_visible(Locators.FLOR).send_keys(flor)
        self.element_is_visible(Locators.CHOOSE_PAYMENT_CASH).click()
        self.element_is_visible(Locators.PHONE).send_keys(phone)
        self.element_is_visible(Locators.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(Locators.SECOND_NAME).send_keys(second_name)
        self.element_is_visible(Locators.THIRD_NAME).send_keys(third_name)
        self.element_is_visible(Locators.COMMENTS).send_keys(comments)
        self.element_is_visible(Locators.DONT_CALL).click()
        # self.element_is_visible(Locators.CHECKOUT).click()
        time.sleep(5)

    def do_new_post_office(self):
        phone = '666666666'
        first_name = 'Denys'
        second_name = 'Budkov'
        third_name = 'Vasylevych'
        comments = 'Test QA'

        self.element_is_visible(Locators.PRODUCT_CARD).click()
        self.element_is_visible(Locators.BUY_ON_STORE_BUTTON).click()
        self.element_is_visible(Locators.CART).click()
        self.element_is_visible(Locators.CHOOSE_NEW_POST_OFFICE).click()
        self.element_is_visible(Locators.CHOOSE_STORE_NEW_POST).click()
        self.element_is_visible(Locators.CHOOSE_PAYMENT_CASH).click()
        self.element_is_visible(Locators.PHONE).send_keys(phone)
        self.element_is_visible(Locators.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(Locators.SECOND_NAME).send_keys(second_name)
        self.element_is_visible(Locators.THIRD_NAME).send_keys(third_name)
        self.element_is_visible(Locators.COMMENTS).send_keys(comments)
        self.element_is_visible(Locators.DONT_CALL).click()
        # self.element_is_visible(Locators.CHECKOUT).click()
        time.sleep(5)

    def do_new_post_office_xyn(self):
        phone = '666666666'
        first_name = 'Denys'
        second_name = 'Budkov'
        third_name = 'Vasylevych'
        comments = 'Test QA'

        self.element_is_visible(Locators.PRODUCT_CARD).click()
        self.element_is_visible(Locators.BUY_ON_STORE_BUTTON).click()
        self.element_is_visible(Locators.CART).click()
        self.element_is_visible(Locators.CHOOSE_NEW_POST_OFFICE).click()
        self.element_is_visible(Locators.CHOOSE_STORE_NEW_POST).click()
        self.element_is_visible(Locators.CHOOSE_PAYMENT_PART).click()
        self.element_is_visible(Locators.CHOOSE_PART_MONO).click()
        self.element_is_visible(Locators.PHONE).send_keys(phone)
        self.element_is_visible(Locators.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(Locators.SECOND_NAME).send_keys(second_name)
        self.element_is_visible(Locators.THIRD_NAME).send_keys(third_name)
        self.element_is_visible(Locators.COMMENTS).send_keys(comments)
        self.element_is_visible(Locators.DONT_CALL).click()
        # self.element_is_visible(Locators.CHECKOUT).click()
        time.sleep(5)

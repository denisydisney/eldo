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
        self.element_is_visible(Locators.CHECKOUT).click()
        thp = self.element_is_visible(Locators.THP)
        if thp == thp:
            print('PASS')
        else:
            print('FAIL')
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
        googlepay = self.element_is_visible(Locators.CHECKOUT_GOOGLEPAY)
        if googlepay == googlepay:
            print('PASS')
        else:
            print('FAIL')
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
        self.element_is_visible(Locators.CHECKOUT).click()
        ipay = self.element_is_visible(Locators.IPAY)
        if ipay == ipay:
            print('PASS')
        else:
            print('FAIL')
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
        self.element_is_visible(Locators.IPN).send_keys(ipn)
        self.element_is_visible(Locators.PHONE).send_keys(phone)
        self.element_is_visible(Locators.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(Locators.SECOND_NAME).send_keys(second_name)
        self.element_is_visible(Locators.THIRD_NAME).send_keys(third_name)
        self.element_is_visible(Locators.COMMENTS).send_keys(comments)
        self.element_is_visible(Locators.DONT_CALL).click()
        self.element_is_visible(Locators.CHECKOUT).click()
        thp = self.element_is_visible(Locators.THP)
        if thp == thp:
            print('PASS')
        else:
            print('FAIL')
        time.sleep(5)

    def pick_up_part_privat(self):
        phone = '637340443'
        first_name = 'Oleh'
        second_name = 'Khondych'
        third_name = 'Viktorovich'
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
        self.element_is_visible(Locators.CHECKOUT).click()
        thp = self.element_is_visible(Locators.THP)
        if thp == thp:
            print('PASS')
        else:
            print('FAIL')
        time.sleep(5)

    def pick_up_part_mono(self):
        phone = '994803905'
        first_name = 'Oleksii'
        second_name = 'Smeshkov'
        third_name = 'Jude'
        email = 'oleksii.smeshkov@eldorado.ua'
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
        self.element_is_visible(Locators.EMAIL).send_keys(email)
        self.element_is_visible(Locators.COMMENTS).send_keys(comments)
        self.element_is_visible(Locators.DONT_CALL).click()
        self.element_is_visible(Locators.CHECKOUT).click()
        monopay = self.element_is_visible(Locators.MONOPAY)
        if monopay == monopay:
            print('PASS')
        else:
            print('FAIL')
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
        self.element_is_visible(Locators.CHECKOUT).click()
        thp = self.element_is_visible(Locators.THP)
        if thp == thp:
            print('PASS')
        else:
            print('FAIL')
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
        self.element_is_visible(Locators.CHECKOUT).click()
        alert = self.element_is_visible(Locators.ALERT)
        if alert != alert:
            print('PASS')
        else:
            print('FAIL')
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
        self.element_is_visible(Locators.CHECKOUT).click()
        thp = self.element_is_visible(Locators.THP)
        if thp == thp:
            print('PASS')
        else:
            print('FAIL')
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
        self.element_is_visible(Locators.CHECKOUT).click()
        globuspay = self.element_is_visible(Locators.THP)
        if globuspay != globuspay:
            print('PASS')
        else:
            print('FAIL')
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
        self.element_is_visible(Locators.CHECKOUT).click()
        thp = self.element_is_visible(Locators.THP)
        if thp == thp:
            print('PASS')
        else:
            print('FAIL')
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
        self.element_is_visible(Locators.CHECKOUT).click()
        alert = self.element_is_visible(Locators.ALERT)
        if alert != alert:
            print('PASS')
        else:
            print('FAIL')
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
        self.element_is_visible(Locators.CHECKOUT).click()
        alert = self.element_is_visible(Locators.ALERT)
        if alert != alert:
            print('PASS')
        else:
            print('FAIL')
        time.sleep(5)

    ####################################################################################################################
    def targeted_cash(self):
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
        self.element_is_visible(Locators.CHECKOUT).click()
        thp = self.element_is_visible(Locators.THP)
        if thp == thp:
            print('PASS')
        else:
            print('FAIL')
        time.sleep(5)

    def targeted_privar24(self):
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
        self.element_is_visible(Locators.CHOOSE_PAYMENT_PRIVA24).click()
        self.element_is_visible(Locators.PHONE).send_keys(phone)
        self.element_is_visible(Locators.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(Locators.SECOND_NAME).send_keys(second_name)
        self.element_is_visible(Locators.THIRD_NAME).send_keys(third_name)
        self.element_is_visible(Locators.COMMENTS).send_keys(comments)
        self.element_is_visible(Locators.DONT_CALL).click()
        self.element_is_visible(Locators.CHECKOUT).click()
        privat24pay = self.element_is_visible(Locators.PRIVAT24PAY)
        if privat24pay == privat24pay:
            print('PASS')
        else:
            print('FAIL')
        time.sleep(5)

    def targeted_googlepay(self):
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
        self.element_is_visible(Locators.CHOOSE_PAYMENT_GOOGLEPAY).click()
        self.element_is_visible(Locators.PHONE).send_keys(phone)
        self.element_is_visible(Locators.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(Locators.SECOND_NAME).send_keys(second_name)
        self.element_is_visible(Locators.THIRD_NAME).send_keys(third_name)
        self.element_is_visible(Locators.COMMENTS).send_keys(comments)
        self.element_is_visible(Locators.DONT_CALL).click()
        googlepay = self.element_is_visible(Locators.CHECKOUT_GOOGLEPAY)
        if googlepay == googlepay:
            print('PASS')
        else:
            print('FAIL')
        time.sleep(5)

    def targeted_anycard(self):
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
        self.element_is_visible(Locators.CHOOSE_PAYMENT_ANY_CARDS).click()
        self.element_is_visible(Locators.PHONE).send_keys(phone)
        self.element_is_visible(Locators.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(Locators.SECOND_NAME).send_keys(second_name)
        self.element_is_visible(Locators.THIRD_NAME).send_keys(third_name)
        self.element_is_visible(Locators.COMMENTS).send_keys(comments)
        self.element_is_visible(Locators.DONT_CALL).click()
        self.element_is_visible(Locators.CHECKOUT).click()
        ipay = self.element_is_visible(Locators.IPAY)
        if ipay == ipay:
            print('PASS')
        else:
            print('FAIL')
        time.sleep(5)

    def targeted_part_super(self):
        ipn = '6666666666'
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
        self.element_is_visible(Locators.CHOOSE_PAYMENT_PART)
        self.element_is_visible(Locators.CHOOSE_PART_SUPER).click()
        self.element_is_visible(Locators.IPN).send_keys(ipn)
        self.element_is_visible(Locators.PHONE).send_keys(phone)
        self.element_is_visible(Locators.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(Locators.SECOND_NAME).send_keys(second_name)
        self.element_is_visible(Locators.THIRD_NAME).send_keys(third_name)
        self.element_is_visible(Locators.COMMENTS).send_keys(comments)
        self.element_is_visible(Locators.DONT_CALL).click()
        self.element_is_visible(Locators.CHECKOUT).click()
        thp = self.element_is_visible(Locators.THP)
        if thp == thp:
            print('PASS')
        else:
            print('FAIL')
        time.sleep(5)

    def targeted_part_privat(self):
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
        self.element_is_visible(Locators.CHOOSE_PAYMENT_PART).click()
        self.element_is_visible(Locators.CHOOSE_PART_PRIVAT).click()
        self.element_is_visible(Locators.PHONE).send_keys(phone)
        self.element_is_visible(Locators.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(Locators.SECOND_NAME).send_keys(second_name)
        self.element_is_visible(Locators.THIRD_NAME).send_keys(third_name)
        self.element_is_visible(Locators.COMMENTS).send_keys(comments)
        self.element_is_visible(Locators.DONT_CALL).click()
        self.element_is_visible(Locators.CHECKOUT).click()
        thp = self.element_is_visible(Locators.THP)
        if thp == thp:
            print('PASS')
        else:
            print('FAIL')
        time.sleep(5)

    def targeted_part_mono(self):
        street = 'Кіото'
        house = '13'
        flat = '80'
        flor = '11'
        phone = '994803905'
        first_name = 'Oleksii'
        second_name = 'Smeshkov'
        third_name = 'Jude'
        email = 'oleksii.smeshkov@eldorado.ua'
        comments = 'Test QA'

        self.element_is_visible(Locators.PRODUCT_CARD).click()
        self.element_is_visible(Locators.BUY_ON_STORE_BUTTON).click()
        self.element_is_visible(Locators.CART).click()
        self.element_is_visible(Locators.CHOOSE_TARGETED_DELIVERY).click()
        self.element_is_visible(Locators.STREET).send_keys(street)
        self.element_is_visible(Locators.HOUSE).send_keys(house)
        self.element_is_visible(Locators.FLAT).send_keys(flat)
        self.element_is_visible(Locators.FLOR).send_keys(flor)
        self.element_is_visible(Locators.CHOOSE_PAYMENT_PART).click()
        self.element_is_visible(Locators.CHOOSE_PART_MONO).click()
        self.element_is_visible(Locators.PHONE).send_keys(phone)
        self.element_is_visible(Locators.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(Locators.SECOND_NAME).send_keys(second_name)
        self.element_is_visible(Locators.THIRD_NAME).send_keys(third_name)
        self.element_is_visible(Locators.EMAIL).send_keys(email)
        self.element_is_visible(Locators.COMMENTS).send_keys(comments)
        self.element_is_visible(Locators.DONT_CALL).click()
        self.element_is_visible(Locators.CHECKOUT).click()
        monopay = self.element_is_visible(Locators.MONOPAY)
        if monopay == monopay:
            print("PASS")
        else:
            print("FAIL")
        time.sleep(5)

    def targeted_part_oschad(self):
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
        self.element_is_visible(Locators.CHOOSE_PAYMENT_PART).click()
        self.element_is_visible(Locators.CHOOSE_PART_OSCHAD).click()
        self.element_is_visible(Locators.PHONE).send_keys(phone)
        self.element_is_visible(Locators.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(Locators.SECOND_NAME).send_keys(second_name)
        self.element_is_visible(Locators.THIRD_NAME).send_keys(third_name)
        self.element_is_visible(Locators.COMMENTS).send_keys(comments)
        self.element_is_visible(Locators.DONT_CALL).click()
        self.element_is_visible(Locators.CHECKOUT).click()
        thp = self.element_is_visible(Locators.THP)
        if thp == thp:
            print('PASS')
        else:
            print('FAIL')
        time.sleep(5)

    def targeted_part_abank(self):
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
        self.element_is_visible(Locators.CHOOSE_PAYMENT_PART).click()
        self.element_is_visible(Locators.CHOOSE_PART_ABANK).click()
        self.element_is_visible(Locators.PHONE).send_keys(phone)
        self.element_is_visible(Locators.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(Locators.SECOND_NAME).send_keys(second_name)
        self.element_is_visible(Locators.THIRD_NAME).send_keys(third_name)
        self.element_is_visible(Locators.COMMENTS).send_keys(comments)
        self.element_is_visible(Locators.DONT_CALL).click()
        self.element_is_visible(Locators.CHECKOUT).click()
        alert = self.element_is_visible(Locators.ALERT)
        if alert != alert:
            print('PASS')
        else:
            print('FAIL')
        time.sleep(5)

    def targeted_part_pumb(self):
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
        self.element_is_visible(Locators.CHOOSE_PAYMENT_PART).click()
        self.element_is_visible(Locators.CHOOSE_PART_PUMB).click()
        self.element_is_visible(Locators.PHONE).send_keys(phone)
        self.element_is_visible(Locators.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(Locators.SECOND_NAME).send_keys(second_name)
        self.element_is_visible(Locators.THIRD_NAME).send_keys(third_name)
        self.element_is_visible(Locators.COMMENTS).send_keys(comments)
        self.element_is_visible(Locators.DONT_CALL).click()
        self.element_is_visible(Locators.CHECKOUT).click()
        thp = self.element_is_visible(Locators.THP)
        if thp == thp:
            print('PASS')
        else:
            print('FAIL')
        time.sleep(5)

    def targeted_part_globus(self):
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
        self.element_is_visible(Locators.CHOOSE_PAYMENT_PART).click()
        self.element_is_visible(Locators.CHOOSE_PART_GLOBUS).click()
        self.element_is_visible(Locators.PHONE).send_keys(phone)
        self.element_is_visible(Locators.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(Locators.SECOND_NAME).send_keys(second_name)
        self.element_is_visible(Locators.THIRD_NAME).send_keys(third_name)
        self.element_is_visible(Locators.COMMENTS).send_keys(comments)
        self.element_is_visible(Locators.DONT_CALL).click()
        self.element_is_visible(Locators.CHECKOUT).click()
        globuspay = self.element_is_visible(Locators.THP)
        if globuspay != globuspay:
            print('PASS')
        else:
            print('FAIL')
        time.sleep(5)

    def targeted_part_otp(self):
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
        self.element_is_visible(Locators.CHOOSE_PAYMENT_PART).click()
        self.element_is_visible(Locators.CHOOSE_PART_OTP).click()
        self.element_is_visible(Locators.PHONE).send_keys(phone)
        self.element_is_visible(Locators.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(Locators.SECOND_NAME).send_keys(second_name)
        self.element_is_visible(Locators.THIRD_NAME).send_keys(third_name)
        self.element_is_visible(Locators.COMMENTS).send_keys(comments)
        self.element_is_visible(Locators.DONT_CALL).click()
        self.element_is_visible(Locators.CHECKOUT).click()
        thp = self.element_is_visible(Locators.THP)
        if thp == thp:
            print('PASS')
        else:
            print('FAIL')
        time.sleep(5)

    def targeted_part_sport(self):
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
        self.element_is_visible(Locators.CHOOSE_PAYMENT_PART).click()
        self.element_is_visible(Locators.CHOOSE_PART_SPORT).click()
        self.element_is_visible(Locators.PHONE).send_keys(phone)
        self.element_is_visible(Locators.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(Locators.SECOND_NAME).send_keys(second_name)
        self.element_is_visible(Locators.THIRD_NAME).send_keys(third_name)
        self.element_is_visible(Locators.COMMENTS).send_keys(comments)
        self.element_is_visible(Locators.DONT_CALL).click()
        self.element_is_visible(Locators.CHECKOUT).click()
        alert = self.element_is_visible(Locators.ALERT)
        if alert != alert:
            print('PASS')
        else:
            print('FAIL')
        time.sleep(5)

    def targeted_part_sense(self):
        street = 'Кіото'
        house = '13'
        flat = '80'
        flor = '11'
        num_card = '6666'
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
        self.element_is_visible(Locators.CHOOSE_PAYMENT_PART).click()
        self.element_is_visible(Locators.CHOOSE_PART_SENSE).click()
        self.element_is_visible(Locators.NUM_CARD).send_keys(num_card)
        self.element_is_visible(Locators.PHONE).send_keys(phone)
        self.element_is_visible(Locators.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(Locators.SECOND_NAME).send_keys(second_name)
        self.element_is_visible(Locators.THIRD_NAME).send_keys(third_name)
        self.element_is_visible(Locators.COMMENTS).send_keys(comments)
        self.element_is_visible(Locators.DONT_CALL).click()
        self.element_is_visible(Locators.CHECKOUT).click()
        alert = self.element_is_visible(Locators.ALERT)
        if alert != alert:
            print('PASS')
        else:
            print('FAIL')
        time.sleep(5)

    ####################################################################################################################
    def new_post_cash(self):
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
        self.element_is_visible(Locators.CHECKOUT).click()
        thp = self.element_is_visible(Locators.THP)
        if thp == thp:
            print('PASS')
        else:
            print('FAIL')
        time.sleep(5)

    def new_post_privat24(self):
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
        self.element_is_visible(Locators.CHOOSE_PAYMENT_PRIVA24).click()
        self.element_is_visible(Locators.PHONE).send_keys(phone)
        self.element_is_visible(Locators.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(Locators.SECOND_NAME).send_keys(second_name)
        self.element_is_visible(Locators.THIRD_NAME).send_keys(third_name)
        self.element_is_visible(Locators.COMMENTS).send_keys(comments)
        self.element_is_visible(Locators.DONT_CALL).click()
        self.element_is_visible(Locators.CHECKOUT).click()
        privat24pay = self.element_is_visible(Locators.PRIVAT24PAY)
        if privat24pay == privat24pay:
            print('PASS')
        else:
            print('FAIL')
        time.sleep(5)

    def new_post_googlepay(self):
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
        self.element_is_visible(Locators.CHOOSE_PAYMENT_GOOGLEPAY).click()
        self.element_is_visible(Locators.PHONE).send_keys(phone)
        self.element_is_visible(Locators.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(Locators.SECOND_NAME).send_keys(second_name)
        self.element_is_visible(Locators.THIRD_NAME).send_keys(third_name)
        self.element_is_visible(Locators.COMMENTS).send_keys(comments)
        self.element_is_visible(Locators.DONT_CALL).click()
        googlepay = self.element_is_visible(Locators.CHECKOUT_GOOGLEPAY)
        if googlepay == googlepay:
            print('PASS')
        else:
            print('FAIL')
        time.sleep(5)

    def new_post_anycards(self):
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
        self.element_is_visible(Locators.CHOOSE_PAYMENT_ANY_CARDS).click()
        self.element_is_visible(Locators.PHONE).send_keys(phone)
        self.element_is_visible(Locators.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(Locators.SECOND_NAME).send_keys(second_name)
        self.element_is_visible(Locators.THIRD_NAME).send_keys(third_name)
        self.element_is_visible(Locators.COMMENTS).send_keys(comments)
        self.element_is_visible(Locators.DONT_CALL).click()
        self.element_is_visible(Locators.CHECKOUT).click()
        ipay = self.element_is_visible(Locators.IPAY)
        if ipay == ipay:
            print('PASS')
        else:
            print('FAIL')
        time.sleep(5)

    def new_post_part_super(self):
        ipn = '6666666666'
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
        self.element_is_visible(Locators.CHOOSE_PART_SUPER).click()
        self.element_is_visible(Locators.IPN).send_keys(ipn)
        self.element_is_visible(Locators.PHONE).send_keys(phone)
        self.element_is_visible(Locators.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(Locators.SECOND_NAME).send_keys(second_name)
        self.element_is_visible(Locators.THIRD_NAME).send_keys(third_name)
        self.element_is_visible(Locators.COMMENTS).send_keys(comments)
        self.element_is_visible(Locators.DONT_CALL).click()
        self.element_is_visible(Locators.CHECKOUT).click()
        thp = self.element_is_visible(Locators.THP)
        if thp == thp:
            print('PASS')
        else:
            print('FAIL')
        time.sleep(5)

    def new_post_part_privat(self):
        phone = '637340443'
        first_name = 'Oleh'
        second_name = 'Khondych'
        third_name = 'Viktorovich'
        comments = 'Test QA'

        self.element_is_visible(Locators.PRODUCT_CARD).click()
        self.element_is_visible(Locators.BUY_ON_STORE_BUTTON).click()
        self.element_is_visible(Locators.CART).click()
        self.element_is_visible(Locators.CHOOSE_NEW_POST_OFFICE).click()
        self.element_is_visible(Locators.CHOOSE_STORE_NEW_POST).click()
        self.element_is_visible(Locators.CHOOSE_PAYMENT_PART).click()
        self.element_is_visible(Locators.CHOOSE_PART_PRIVAT).click()
        self.element_is_visible(Locators.PHONE).send_keys(phone)
        self.element_is_visible(Locators.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(Locators.SECOND_NAME).send_keys(second_name)
        self.element_is_visible(Locators.THIRD_NAME).send_keys(third_name)
        self.element_is_visible(Locators.COMMENTS).send_keys(comments)
        self.element_is_visible(Locators.DONT_CALL).click()
        self.element_is_visible(Locators.CHECKOUT).click()
        thp = self.element_is_visible(Locators.THP)
        if thp == thp:
            print('PASS')
        else:
            print('FAIL')
        time.sleep(5)

    def new_post_part_mono(self):
        phone = '994803905'
        first_name = 'Oleksii'
        second_name = 'Smeshkov'
        third_name = 'Jude'
        email = 'oleksii.smeshkov@eldorado.ua'
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
        self.element_is_visible(Locators.EMAIL).send_keys(email)
        self.element_is_visible(Locators.COMMENTS).send_keys(comments)
        self.element_is_visible(Locators.DONT_CALL).click()
        self.element_is_visible(Locators.CHECKOUT).click()
        monopay = self.element_is_visible(Locators.MONOPAY)
        if monopay == monopay:
            print('PASS')
        else:
            print('FAIL')
        time.sleep(5)

    def new_post_part_oschad(self):
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
        self.element_is_visible(Locators.CHOOSE_PART_OSCHAD).click()
        self.element_is_visible(Locators.PHONE).send_keys(phone)
        self.element_is_visible(Locators.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(Locators.SECOND_NAME).send_keys(second_name)
        self.element_is_visible(Locators.THIRD_NAME).send_keys(third_name)
        self.element_is_visible(Locators.COMMENTS).send_keys(comments)
        self.element_is_visible(Locators.DONT_CALL).click()
        self.element_is_visible(Locators.CHECKOUT).click()
        thp = self.element_is_visible(Locators.THP)
        if thp == thp:
            print('PASS')
        else:
            print('FAIL')
        time.sleep(5)

    def new_post_part_abank(self):
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
        self.element_is_visible(Locators.CHOOSE_PART_ABANK).click()
        self.element_is_visible(Locators.PHONE).send_keys(phone)
        self.element_is_visible(Locators.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(Locators.SECOND_NAME).send_keys(second_name)
        self.element_is_visible(Locators.THIRD_NAME).send_keys(third_name)
        self.element_is_visible(Locators.COMMENTS).send_keys(comments)
        self.element_is_visible(Locators.DONT_CALL).click()
        self.element_is_visible(Locators.CHECKOUT).click()
        alert = self.element_is_visible(Locators.ALERT)
        if alert != alert:
            print('PASS')
        else:
            print('FAIL')
        time.sleep(5)

    def new_post_part_punb(self):
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
        self.element_is_visible(Locators.CHOOSE_PART_PUMB).click()
        self.element_is_visible(Locators.PHONE).send_keys(phone)
        self.element_is_visible(Locators.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(Locators.SECOND_NAME).send_keys(second_name)
        self.element_is_visible(Locators.THIRD_NAME).send_keys(third_name)
        self.element_is_visible(Locators.COMMENTS).send_keys(comments)
        self.element_is_visible(Locators.DONT_CALL).click()
        self.element_is_visible(Locators.CHECKOUT).click()
        thp = self.element_is_visible(Locators.THP)
        if thp == thp:
            print('PASS')
        else:
            print('FAIL')
        time.sleep(5)

    def new_post_part_globus(self):
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
        self.element_is_visible(Locators.CHOOSE_PART_GLOBUS).click()
        self.element_is_visible(Locators.PHONE).send_keys(phone)
        self.element_is_visible(Locators.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(Locators.SECOND_NAME).send_keys(second_name)
        self.element_is_visible(Locators.THIRD_NAME).send_keys(third_name)
        self.element_is_visible(Locators.COMMENTS).send_keys(comments)
        self.element_is_visible(Locators.DONT_CALL).click()
        self.element_is_visible(Locators.CHECKOUT).click()
        globuspay = self.element_is_visible(Locators.THP)
        if globuspay != globuspay:
            print('PASS')
        else:
            print('FAIL')
        time.sleep(5)

    def new_post_part_otp(self):
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
        self.element_is_visible(Locators.CHOOSE_PART_OTP).click()
        self.element_is_visible(Locators.PHONE).send_keys(phone)
        self.element_is_visible(Locators.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(Locators.SECOND_NAME).send_keys(second_name)
        self.element_is_visible(Locators.THIRD_NAME).send_keys(third_name)
        self.element_is_visible(Locators.COMMENTS).send_keys(comments)
        self.element_is_visible(Locators.DONT_CALL).click()
        self.element_is_visible(Locators.CHECKOUT).click()
        thp = self.element_is_visible(Locators.THP)
        if thp == thp:
            print('PASS')
        else:
            print('FAIL')
        time.sleep(5)

    def new_post_part_sport(self):
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
        self.element_is_visible(Locators.CHOOSE_PART_SPORT).click()
        self.element_is_visible(Locators.PHONE).send_keys(phone)
        self.element_is_visible(Locators.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(Locators.SECOND_NAME).send_keys(second_name)
        self.element_is_visible(Locators.THIRD_NAME).send_keys(third_name)
        self.element_is_visible(Locators.COMMENTS).send_keys(comments)
        self.element_is_visible(Locators.DONT_CALL).click()
        self.element_is_visible(Locators.CHECKOUT).click()
        alert = self.element_is_visible(Locators.ALERT)
        if alert != alert:
            print('PASS')
        else:
            print('FAIL')
        time.sleep(5)

    def new_post_part_sense(self):
        num_card = '6666'
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
        self.element_is_visible(Locators.CHOOSE_PART_SENSE).click()
        self.element_is_visible(Locators.NUM_CARD).send_keys(num_card)
        self.element_is_visible(Locators.PHONE).send_keys(phone)
        self.element_is_visible(Locators.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(Locators.SECOND_NAME).send_keys(second_name)
        self.element_is_visible(Locators.THIRD_NAME).send_keys(third_name)
        self.element_is_visible(Locators.COMMENTS).send_keys(comments)
        self.element_is_visible(Locators.DONT_CALL).click()
        self.element_is_visible(Locators.CHECKOUT).click()
        alert = self.element_is_visible(Locators.ALERT)
        if alert != alert:
            print('PASS')
        else:
            print('FAIL')
        time.sleep(5)


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
        re_captcha = self.element_is_visible(Locators.RE_CAPTCHA).click()
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

import time
from pages.base_page import BasePage
from locatros.order_page_locators import OrderPageLocators as Locators
from locatros.order_variables import OrderVariablesLocators as OVL


class OrderPage(BasePage):
    def pick_up_cash(self):

        self.element_is_visible(Locators.PRODUCT_CARD).click()
        self.element_is_visible(Locators.BUY_ON_STORE_BUTTON).click()
        self.element_is_visible(Locators.CART).click()
        self.element_is_visible(Locators.CHOOSE_PICK_UP_FROM_STORE).click()
        self.element_is_visible(Locators.CHOOSE_STORE_PICK_UP).click()
        self.element_is_visible(Locators.CHOOSE_PAYMENT_CASH).click()
        self.element_is_visible(Locators.PHONE).send_keys(OVL.phone)
        self.element_is_visible(Locators.FIRST_NAME).send_keys(OVL.first_name)
        self.element_is_visible(Locators.COMMENTS).send_keys(OVL.comments)
        self.element_is_visible(Locators.DONT_CALL).click()
        self.element_is_visible(Locators.CHECKOUT).click()
        thp = self.element_is_visible(Locators.THP)
        if thp == thp:
            print('PASS')
        else:
            print('FAIL')
        time.sleep(5)

    def pick_up_googlepay(self):

        self.element_is_visible(Locators.PRODUCT_CARD).click()
        self.element_is_visible(Locators.BUY_ON_STORE_BUTTON).click()
        self.element_is_visible(Locators.CART).click()
        self.element_is_visible(Locators.CHOOSE_PICK_UP_FROM_STORE).click()
        self.element_is_visible(Locators.CHOOSE_STORE_PICK_UP).click()
        self.element_is_visible(Locators.CHOOSE_PAYMENT_GOOGLEPAY).click()
        self.element_is_visible(Locators.PHONE).send_keys(OVL.phone)
        self.element_is_visible(Locators.FIRST_NAME).send_keys(OVL.first_name)
        self.element_is_visible(Locators.SECOND_NAME).send_keys(OVL.second_name)
        self.element_is_visible(Locators.THIRD_NAME).send_keys(OVL.third_name)
        self.element_is_visible(Locators.COMMENTS).send_keys(OVL.comments)
        self.element_is_visible(Locators.DONT_CALL).click()
        googlepay = self.element_is_visible(Locators.CHECKOUT_GOOGLEPAY)
        if googlepay == googlepay:
            print('PASS')
        else:
            print('FAIL')
        time.sleep(5)

    def pick_up_anycards(self):

        self.element_is_visible(Locators.PRODUCT_CARD).click()
        self.element_is_visible(Locators.BUY_ON_STORE_BUTTON).click()
        self.element_is_visible(Locators.CART).click()
        self.element_is_visible(Locators.CHOOSE_PICK_UP_FROM_STORE).click()
        self.element_is_visible(Locators.CHOOSE_STORE_PICK_UP).click()
        self.element_is_visible(Locators.CHOOSE_PAYMENT_ANY_CARDS).click()
        self.element_is_visible(Locators.PHONE).send_keys(OVL.phone)
        self.element_is_visible(Locators.FIRST_NAME).send_keys(OVL.first_name)
        self.element_is_visible(Locators.SECOND_NAME).send_keys(OVL.second_name)
        self.element_is_visible(Locators.THIRD_NAME).send_keys(OVL.third_name)
        self.element_is_visible(Locators.COMMENTS).send_keys(OVL.comments)
        self.element_is_visible(Locators.DONT_CALL).click()
        self.element_is_visible(Locators.CHECKOUT).click()
        ipay = self.element_is_visible(Locators.IPAY)
        if ipay == ipay:
            print('PASS')
        else:
            print('FAIL')
        time.sleep(5)

    def pick_up_part_super(self):

        self.element_is_visible(Locators.PRODUCT_CARD).click()
        self.element_is_visible(Locators.BUY_ON_STORE_BUTTON).click()
        self.element_is_visible(Locators.CART).click()
        self.element_is_visible(Locators.CHOOSE_PICK_UP_FROM_STORE).click()
        self.element_is_visible(Locators.CHOOSE_STORE_PICK_UP).click()
        self.element_is_visible(Locators.CHOOSE_PAYMENT_PART).click()
        self.element_is_visible(Locators.CHOOSE_PART_SUPER).click()
        self.element_is_visible(Locators.IPN).send_keys(OVL.ipn)
        self.element_is_visible(Locators.PHONE).send_keys(OVL.phone)
        self.element_is_visible(Locators.FIRST_NAME).send_keys(OVL.first_name)
        self.element_is_visible(Locators.SECOND_NAME).send_keys(OVL.second_name)
        self.element_is_visible(Locators.THIRD_NAME).send_keys(OVL.third_name)
        self.element_is_visible(Locators.COMMENTS).send_keys(OVL.comments)
        self.element_is_visible(Locators.DONT_CALL).click()
        self.element_is_visible(Locators.CHECKOUT).click()
        thp = self.element_is_visible(Locators.THP)
        if thp == thp:
            print('PASS')
        else:
            print('FAIL')
        time.sleep(5)

    def pick_up_part_privat(self):

        self.element_is_visible(Locators.PRODUCT_CARD).click()
        self.element_is_visible(Locators.BUY_ON_STORE_BUTTON).click()
        self.element_is_visible(Locators.CART).click()
        self.element_is_visible(Locators.CHOOSE_PICK_UP_FROM_STORE).click()
        self.element_is_visible(Locators.CHOOSE_STORE_PICK_UP).click()
        self.element_is_visible(Locators.CHOOSE_PAYMENT_PART).click()
        self.element_is_visible(Locators.CHOOSE_PART_PRIVAT).click()
        self.element_is_visible(Locators.PHONE).send_keys(OVL.phone)
        self.element_is_visible(Locators.FIRST_NAME).send_keys(OVL.first_name)
        self.element_is_visible(Locators.SECOND_NAME).send_keys(OVL.second_name)
        self.element_is_visible(Locators.THIRD_NAME).send_keys(OVL.third_name)
        self.element_is_visible(Locators.COMMENTS).send_keys(OVL.comments)
        self.element_is_visible(Locators.DONT_CALL).click()
        self.element_is_visible(Locators.CHECKOUT).click()
        thp = self.element_is_visible(Locators.THP)
        if thp == thp:
            print('PASS')
        else:
            print('FAIL')
        time.sleep(5)

    def pick_up_part_mono(self):

        self.element_is_visible(Locators.PRODUCT_CARD).click()
        self.element_is_visible(Locators.BUY_ON_STORE_BUTTON).click()
        self.element_is_visible(Locators.CART).click()
        self.element_is_visible(Locators.CHOOSE_PICK_UP_FROM_STORE).click()
        self.element_is_visible(Locators.CHOOSE_STORE_PICK_UP).click()
        self.element_is_visible(Locators.CHOOSE_PAYMENT_PART).click()
        self.element_is_visible(Locators.CHOOSE_PART_MONO).click()
        self.element_is_visible(Locators.PHONE).send_keys(OVL.s_phone)
        self.element_is_visible(Locators.FIRST_NAME).send_keys(OVL.s_first_name)
        self.element_is_visible(Locators.SECOND_NAME).send_keys(OVL.s_second_name)
        self.element_is_visible(Locators.THIRD_NAME).send_keys(OVL.s_third_name)
        self.element_is_visible(Locators.EMAIL).send_keys(OVL.s_email)
        self.element_is_visible(Locators.COMMENTS).send_keys(OVL.comments)
        self.element_is_visible(Locators.DONT_CALL).click()
        self.element_is_visible(Locators.CHECKOUT).click()
        monopay = self.element_is_visible(Locators.MONOPAY)
        if monopay == monopay:
            print('PASS')
        else:
            print('FAIL')
        time.sleep(5)

    def pick_up_part_oschad(self):

        self.element_is_visible(Locators.PRODUCT_CARD).click()
        self.element_is_visible(Locators.BUY_ON_STORE_BUTTON).click()
        self.element_is_visible(Locators.CART).click()
        self.element_is_visible(Locators.CHOOSE_PICK_UP_FROM_STORE).click()
        self.element_is_visible(Locators.CHOOSE_STORE_PICK_UP).click()
        self.element_is_visible(Locators.CHOOSE_PAYMENT_PART).click()
        self.element_is_visible(Locators.CHOOSE_PART_OSCHAD).click()
        self.element_is_visible(Locators.PHONE).send_keys(OVL.phone)
        self.element_is_visible(Locators.FIRST_NAME).send_keys(OVL.first_name)
        self.element_is_visible(Locators.SECOND_NAME).send_keys(OVL.second_name)
        self.element_is_visible(Locators.THIRD_NAME).send_keys(OVL.third_name)
        self.element_is_visible(Locators.COMMENTS).send_keys(OVL.comments)
        self.element_is_visible(Locators.DONT_CALL).click()
        self.element_is_visible(Locators.CHECKOUT).click()
        thp = self.element_is_visible(Locators.THP)
        if thp == thp:
            print('PASS')
        else:
            print('FAIL')
        time.sleep(5)

    def pick_up_part_abank(self):

        self.element_is_visible(Locators.PRODUCT_CARD).click()
        self.element_is_visible(Locators.BUY_ON_STORE_BUTTON).click()
        self.element_is_visible(Locators.CART).click()
        self.element_is_visible(Locators.CHOOSE_PICK_UP_FROM_STORE).click()
        self.element_is_visible(Locators.CHOOSE_STORE_PICK_UP).click()
        self.element_is_visible(Locators.CHOOSE_PAYMENT_PART).click()
        self.element_is_visible(Locators.CHOOSE_PART_ABANK).click()
        self.element_is_visible(Locators.PHONE).send_keys(OVL.phone)
        self.element_is_visible(Locators.FIRST_NAME).send_keys(OVL.first_name)
        self.element_is_visible(Locators.SECOND_NAME).send_keys(OVL.second_name)
        self.element_is_visible(Locators.THIRD_NAME).send_keys(OVL.third_name)
        self.element_is_visible(Locators.COMMENTS).send_keys(OVL.comments)
        self.element_is_visible(Locators.DONT_CALL).click()
        self.element_is_visible(Locators.CHECKOUT).click()
        alert = self.element_is_visible(Locators.ALERT)
        if alert != alert:
            print('PASS')
        else:
            print('FAIL')
        time.sleep(5)

    def pick_up_part_punb(self):

        self.element_is_visible(Locators.PRODUCT_CARD).click()
        self.element_is_visible(Locators.BUY_ON_STORE_BUTTON).click()
        self.element_is_visible(Locators.CART).click()
        self.element_is_visible(Locators.CHOOSE_PICK_UP_FROM_STORE).click()
        self.element_is_visible(Locators.CHOOSE_STORE_PICK_UP).click()
        self.element_is_visible(Locators.CHOOSE_PAYMENT_PART).click()
        self.element_is_visible(Locators.CHOOSE_PART_PUMB).click()
        self.element_is_visible(Locators.PHONE).send_keys(OVL.phone)
        self.element_is_visible(Locators.FIRST_NAME).send_keys(OVL.first_name)
        self.element_is_visible(Locators.SECOND_NAME).send_keys(OVL.second_name)
        self.element_is_visible(Locators.THIRD_NAME).send_keys(OVL.third_name)
        self.element_is_visible(Locators.COMMENTS).send_keys(OVL.comments)
        self.element_is_visible(Locators.DONT_CALL).click()
        self.element_is_visible(Locators.CHECKOUT).click()
        thp = self.element_is_visible(Locators.THP)
        if thp == thp:
            print('PASS')
        else:
            print('FAIL')
        time.sleep(5)

    def pick_up_part_globus(self):

        self.element_is_visible(Locators.PRODUCT_CARD).click()
        self.element_is_visible(Locators.BUY_ON_STORE_BUTTON).click()
        self.element_is_visible(Locators.CART).click()
        self.element_is_visible(Locators.CHOOSE_PICK_UP_FROM_STORE).click()
        self.element_is_visible(Locators.CHOOSE_STORE_PICK_UP).click()
        self.element_is_visible(Locators.CHOOSE_PAYMENT_PART).click()
        self.element_is_visible(Locators.CHOOSE_PART_GLOBUS).click()
        self.element_is_visible(Locators.PHONE).send_keys(OVL.phone)
        self.element_is_visible(Locators.FIRST_NAME).send_keys(OVL.first_name)
        self.element_is_visible(Locators.SECOND_NAME).send_keys(OVL.second_name)
        self.element_is_visible(Locators.THIRD_NAME).send_keys(OVL.third_name)
        self.element_is_visible(Locators.COMMENTS).send_keys(OVL.comments)
        self.element_is_visible(Locators.DONT_CALL).click()
        self.element_is_visible(Locators.CHECKOUT).click()
        globuspay = self.element_is_visible(Locators.THP)
        if globuspay != globuspay:
            print('PASS')
        else:
            print('FAIL')
        time.sleep(5)

    def pick_up_part_otp(self):

        self.element_is_visible(Locators.PRODUCT_CARD).click()
        self.element_is_visible(Locators.BUY_ON_STORE_BUTTON).click()
        self.element_is_visible(Locators.CART).click()
        self.element_is_visible(Locators.CHOOSE_PICK_UP_FROM_STORE).click()
        self.element_is_visible(Locators.CHOOSE_STORE_PICK_UP).click()
        self.element_is_visible(Locators.CHOOSE_PAYMENT_PART).click()
        self.element_is_visible(Locators.CHOOSE_PART_OTP).click()
        self.element_is_visible(Locators.PHONE).send_keys(OVL.phone)
        self.element_is_visible(Locators.FIRST_NAME).send_keys(OVL.first_name)
        self.element_is_visible(Locators.SECOND_NAME).send_keys(OVL.second_name)
        self.element_is_visible(Locators.THIRD_NAME).send_keys(OVL.third_name)
        self.element_is_visible(Locators.COMMENTS).send_keys(OVL.comments)
        self.element_is_visible(Locators.DONT_CALL).click()
        self.element_is_visible(Locators.CHECKOUT).click()
        thp = self.element_is_visible(Locators.THP)
        if thp == thp:
            print('PASS')
        else:
            print('FAIL')
        time.sleep(5)

    def pick_up_part_sport(self):

        self.element_is_visible(Locators.PRODUCT_CARD).click()
        self.element_is_visible(Locators.BUY_ON_STORE_BUTTON).click()
        self.element_is_visible(Locators.CART).click()
        self.element_is_visible(Locators.CHOOSE_PICK_UP_FROM_STORE).click()
        self.element_is_visible(Locators.CHOOSE_STORE_PICK_UP).click()
        self.element_is_visible(Locators.CHOOSE_PAYMENT_PART).click()
        self.element_is_visible(Locators.CHOOSE_PART_SPORT).click()
        self.element_is_visible(Locators.PHONE).send_keys(OVL.phone)
        self.element_is_visible(Locators.FIRST_NAME).send_keys(OVL.first_name)
        self.element_is_visible(Locators.SECOND_NAME).send_keys(OVL.second_name)
        self.element_is_visible(Locators.THIRD_NAME).send_keys(OVL.third_name)
        self.element_is_visible(Locators.COMMENTS).send_keys(OVL.comments)
        self.element_is_visible(Locators.DONT_CALL).click()
        self.element_is_visible(Locators.CHECKOUT).click()
        alert = self.element_is_visible(Locators.ALERT)
        if alert != alert:
            print('PASS')
        else:
            print('FAIL')
        time.sleep(5)

    def pick_up_part_sense(self):

        self.element_is_visible(Locators.PRODUCT_CARD).click()
        self.element_is_visible(Locators.BUY_ON_STORE_BUTTON).click()
        self.element_is_visible(Locators.CART).click()
        self.element_is_visible(Locators.CHOOSE_PICK_UP_FROM_STORE).click()
        self.element_is_visible(Locators.CHOOSE_STORE_PICK_UP).click()
        self.element_is_visible(Locators.CHOOSE_PAYMENT_PART).click()
        self.element_is_visible(Locators.CHOOSE_PART_SENSE).click()
        self.element_is_visible(Locators.NUM_CARD).send_keys(OVL.num_card)
        self.element_is_visible(Locators.PHONE).send_keys(OVL.phone)
        self.element_is_visible(Locators.FIRST_NAME).send_keys(OVL.first_name)
        self.element_is_visible(Locators.SECOND_NAME).send_keys(OVL.second_name)
        self.element_is_visible(Locators.THIRD_NAME).send_keys(OVL.third_name)
        self.element_is_visible(Locators.COMMENTS).send_keys(OVL.comments)
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

        self.element_is_visible(Locators.PRODUCT_CARD).click()
        self.element_is_visible(Locators.BUY_ON_STORE_BUTTON).click()
        self.element_is_visible(Locators.CART).click()
        self.element_is_visible(Locators.CHOOSE_TARGETED_DELIVERY).click()
        self.element_is_visible(Locators.STREET).send_keys(OVL.street)
        self.element_is_visible(Locators.HOUSE).send_keys(OVL.house)
        self.element_is_visible(Locators.FLAT).send_keys(OVL.flat)
        self.element_is_visible(Locators.FLOR).send_keys(OVL.flor)
        self.element_is_visible(Locators.CHOOSE_PAYMENT_CASH).click()
        self.element_is_visible(Locators.PHONE).send_keys(OVL.phone)
        self.element_is_visible(Locators.FIRST_NAME).send_keys(OVL.first_name)
        self.element_is_visible(Locators.SECOND_NAME).send_keys(OVL.second_name)
        self.element_is_visible(Locators.THIRD_NAME).send_keys(OVL.third_name)
        self.element_is_visible(Locators.COMMENTS).send_keys(OVL.comments)
        self.element_is_visible(Locators.DONT_CALL).click()
        self.element_is_visible(Locators.CHECKOUT).click()
        thp = self.element_is_visible(Locators.THP)
        if thp == thp:
            print('PASS')
        else:
            print('FAIL')
        time.sleep(5)

    def targeted_privar24(self):

        self.element_is_visible(Locators.PRODUCT_CARD).click()
        self.element_is_visible(Locators.BUY_ON_STORE_BUTTON).click()
        self.element_is_visible(Locators.CART).click()
        self.element_is_visible(Locators.CHOOSE_TARGETED_DELIVERY).click()
        self.element_is_visible(Locators.STREET).send_keys(OVL.street)
        self.element_is_visible(Locators.HOUSE).send_keys(OVL.house)
        self.element_is_visible(Locators.FLAT).send_keys(OVL.flat)
        self.element_is_visible(Locators.FLOR).send_keys(OVL.flor)
        self.element_is_visible(Locators.CHOOSE_PAYMENT_PRIVA24).click()
        self.element_is_visible(Locators.PHONE).send_keys(OVL.phone)
        self.element_is_visible(Locators.FIRST_NAME).send_keys(OVL.first_name)
        self.element_is_visible(Locators.SECOND_NAME).send_keys(OVL.second_name)
        self.element_is_visible(Locators.THIRD_NAME).send_keys(OVL.third_name)
        self.element_is_visible(Locators.COMMENTS).send_keys(OVL.comments)
        self.element_is_visible(Locators.DONT_CALL).click()
        self.element_is_visible(Locators.CHECKOUT).click()
        privat24pay = self.element_is_visible(Locators.PRIVAT24PAY)
        if privat24pay == privat24pay:
            print('PASS')
        else:
            print('FAIL')
        time.sleep(5)

    def targeted_googlepay(self):

        self.element_is_visible(Locators.PRODUCT_CARD).click()
        self.element_is_visible(Locators.BUY_ON_STORE_BUTTON).click()
        self.element_is_visible(Locators.CART).click()
        self.element_is_visible(Locators.CHOOSE_TARGETED_DELIVERY).click()
        self.element_is_visible(Locators.STREET).send_keys(OVL.street)
        self.element_is_visible(Locators.HOUSE).send_keys(OVL.house)
        self.element_is_visible(Locators.FLAT).send_keys(OVL.flat)
        self.element_is_visible(Locators.FLOR).send_keys(OVL.flor)
        self.element_is_visible(Locators.CHOOSE_PAYMENT_GOOGLEPAY).click()
        self.element_is_visible(Locators.PHONE).send_keys(OVL.phone)
        self.element_is_visible(Locators.FIRST_NAME).send_keys(OVL.first_name)
        self.element_is_visible(Locators.SECOND_NAME).send_keys(OVL.second_name)
        self.element_is_visible(Locators.THIRD_NAME).send_keys(OVL.third_name)
        self.element_is_visible(Locators.COMMENTS).send_keys(OVL.comments)
        self.element_is_visible(Locators.DONT_CALL).click()
        googlepay = self.element_is_visible(Locators.CHECKOUT_GOOGLEPAY)
        if googlepay == googlepay:
            print('PASS')
        else:
            print('FAIL')
        time.sleep(5)

    def targeted_anycard(self):

        self.element_is_visible(Locators.PRODUCT_CARD).click()
        self.element_is_visible(Locators.BUY_ON_STORE_BUTTON).click()
        self.element_is_visible(Locators.CART).click()
        self.element_is_visible(Locators.CHOOSE_TARGETED_DELIVERY).click()
        self.element_is_visible(Locators.STREET).send_keys(OVL.street)
        self.element_is_visible(Locators.HOUSE).send_keys(OVL.house)
        self.element_is_visible(Locators.FLAT).send_keys(OVL.flat)
        self.element_is_visible(Locators.FLOR).send_keys(OVL.flor)
        self.element_is_visible(Locators.CHOOSE_PAYMENT_ANY_CARDS).click()
        self.element_is_visible(Locators.PHONE).send_keys(OVL.phone)
        self.element_is_visible(Locators.FIRST_NAME).send_keys(OVL.first_name)
        self.element_is_visible(Locators.SECOND_NAME).send_keys(OVL.second_name)
        self.element_is_visible(Locators.THIRD_NAME).send_keys(OVL.third_name)
        self.element_is_visible(Locators.COMMENTS).send_keys(OVL.comments)
        self.element_is_visible(Locators.DONT_CALL).click()
        self.element_is_visible(Locators.CHECKOUT).click()
        ipay = self.element_is_visible(Locators.IPAY)
        if ipay == ipay:
            print('PASS')
        else:
            print('FAIL')
        time.sleep(5)

    def targeted_part_super(self):

        self.element_is_visible(Locators.PRODUCT_CARD).click()
        self.element_is_visible(Locators.BUY_ON_STORE_BUTTON).click()
        self.element_is_visible(Locators.CART).click()
        self.element_is_visible(Locators.CHOOSE_TARGETED_DELIVERY).click()
        self.element_is_visible(Locators.STREET).send_keys(OVL.street)
        self.element_is_visible(Locators.HOUSE).send_keys(OVL.house)
        self.element_is_visible(Locators.FLAT).send_keys(OVL.flat)
        self.element_is_visible(Locators.FLOR).send_keys(OVL.flor)
        self.element_is_visible(Locators.CHOOSE_PAYMENT_PART)
        self.element_is_visible(Locators.CHOOSE_PART_SUPER).click()
        self.element_is_visible(Locators.IPN).send_keys(OVL.ipn)
        self.element_is_visible(Locators.PHONE).send_keys(OVL.phone)
        self.element_is_visible(Locators.FIRST_NAME).send_keys(OVL.first_name)
        self.element_is_visible(Locators.SECOND_NAME).send_keys(OVL.second_name)
        self.element_is_visible(Locators.THIRD_NAME).send_keys(OVL.third_name)
        self.element_is_visible(Locators.COMMENTS).send_keys(OVL.comments)
        self.element_is_visible(Locators.DONT_CALL).click()
        self.element_is_visible(Locators.CHECKOUT).click()
        thp = self.element_is_visible(Locators.THP)
        if thp == thp:
            print('PASS')
        else:
            print('FAIL')
        time.sleep(5)

    def targeted_part_privat(self):

        self.element_is_visible(Locators.PRODUCT_CARD).click()
        self.element_is_visible(Locators.BUY_ON_STORE_BUTTON).click()
        self.element_is_visible(Locators.CART).click()
        self.element_is_visible(Locators.CHOOSE_TARGETED_DELIVERY).click()
        self.element_is_visible(Locators.STREET).send_keys(OVL.street)
        self.element_is_visible(Locators.HOUSE).send_keys(OVL.house)
        self.element_is_visible(Locators.FLAT).send_keys(OVL.flat)
        self.element_is_visible(Locators.FLOR).send_keys(OVL.flor)
        self.element_is_visible(Locators.CHOOSE_PAYMENT_PART).click()
        self.element_is_visible(Locators.CHOOSE_PART_PRIVAT).click()
        self.element_is_visible(Locators.PHONE).send_keys(OVL.phone)
        self.element_is_visible(Locators.FIRST_NAME).send_keys(OVL.first_name)
        self.element_is_visible(Locators.SECOND_NAME).send_keys(OVL.second_name)
        self.element_is_visible(Locators.THIRD_NAME).send_keys(OVL.third_name)
        self.element_is_visible(Locators.COMMENTS).send_keys(OVL.comments)
        self.element_is_visible(Locators.DONT_CALL).click()
        self.element_is_visible(Locators.CHECKOUT).click()
        thp = self.element_is_visible(Locators.THP)
        if thp == thp:
            print('PASS')
        else:
            print('FAIL')
        time.sleep(5)

    def targeted_part_mono(self):

        self.element_is_visible(Locators.PRODUCT_CARD).click()
        self.element_is_visible(Locators.BUY_ON_STORE_BUTTON).click()
        self.element_is_visible(Locators.CART).click()
        self.element_is_visible(Locators.CHOOSE_TARGETED_DELIVERY).click()
        self.element_is_visible(Locators.STREET).send_keys(OVL.street)
        self.element_is_visible(Locators.HOUSE).send_keys(OVL.house)
        self.element_is_visible(Locators.FLAT).send_keys(OVL.flat)
        self.element_is_visible(Locators.FLOR).send_keys(OVL.flor)
        self.element_is_visible(Locators.CHOOSE_PAYMENT_PART).click()
        self.element_is_visible(Locators.CHOOSE_PART_MONO).click()
        self.element_is_visible(Locators.PHONE).send_keys(OVL.phone)
        self.element_is_visible(Locators.FIRST_NAME).send_keys(OVL.first_name)
        self.element_is_visible(Locators.SECOND_NAME).send_keys(OVL.second_name)
        self.element_is_visible(Locators.THIRD_NAME).send_keys(OVL.third_name)
        self.element_is_visible(Locators.EMAIL).send_keys(OVL.email)
        self.element_is_visible(Locators.COMMENTS).send_keys(OVL.comments)
        self.element_is_visible(Locators.DONT_CALL).click()
        self.element_is_visible(Locators.CHECKOUT).click()
        monopay = self.element_is_visible(Locators.MONOPAY)
        if monopay == monopay:
            print("PASS")
        else:
            print("FAIL")
        time.sleep(5)

    def targeted_part_oschad(self):

        self.element_is_visible(Locators.PRODUCT_CARD).click()
        self.element_is_visible(Locators.BUY_ON_STORE_BUTTON).click()
        self.element_is_visible(Locators.CART).click()
        self.element_is_visible(Locators.CHOOSE_TARGETED_DELIVERY).click()
        self.element_is_visible(Locators.STREET).send_keys(OVL.street)
        self.element_is_visible(Locators.HOUSE).send_keys(OVL.house)
        self.element_is_visible(Locators.FLAT).send_keys(OVL.flat)
        self.element_is_visible(Locators.FLOR).send_keys(OVL.flor)
        self.element_is_visible(Locators.CHOOSE_PAYMENT_PART).click()
        self.element_is_visible(Locators.CHOOSE_PART_OSCHAD).click()
        self.element_is_visible(Locators.PHONE).send_keys(OVL.phone)
        self.element_is_visible(Locators.FIRST_NAME).send_keys(OVL.first_name)
        self.element_is_visible(Locators.SECOND_NAME).send_keys(OVL.second_name)
        self.element_is_visible(Locators.THIRD_NAME).send_keys(OVL.third_name)
        self.element_is_visible(Locators.COMMENTS).send_keys(OVL.comments)
        self.element_is_visible(Locators.DONT_CALL).click()
        self.element_is_visible(Locators.CHECKOUT).click()
        thp = self.element_is_visible(Locators.THP)
        if thp == thp:
            print('PASS')
        else:
            print('FAIL')
        time.sleep(5)

    def targeted_part_abank(self):

        self.element_is_visible(Locators.PRODUCT_CARD).click()
        self.element_is_visible(Locators.BUY_ON_STORE_BUTTON).click()
        self.element_is_visible(Locators.CART).click()
        self.element_is_visible(Locators.CHOOSE_TARGETED_DELIVERY).click()
        self.element_is_visible(Locators.STREET).send_keys(OVL.street)
        self.element_is_visible(Locators.HOUSE).send_keys(OVL.house)
        self.element_is_visible(Locators.FLAT).send_keys(OVL.flat)
        self.element_is_visible(Locators.FLOR).send_keys(OVL.flor)
        self.element_is_visible(Locators.CHOOSE_PAYMENT_PART).click()
        self.element_is_visible(Locators.CHOOSE_PART_ABANK).click()
        self.element_is_visible(Locators.PHONE).send_keys(OVL.phone)
        self.element_is_visible(Locators.FIRST_NAME).send_keys(OVL.first_name)
        self.element_is_visible(Locators.SECOND_NAME).send_keys(OVL.second_name)
        self.element_is_visible(Locators.THIRD_NAME).send_keys(OVL.third_name)
        self.element_is_visible(Locators.COMMENTS).send_keys(OVL.comments)
        self.element_is_visible(Locators.DONT_CALL).click()
        self.element_is_visible(Locators.CHECKOUT).click()
        alert = self.element_is_visible(Locators.ALERT)
        if alert != alert:
            print('PASS')
        else:
            print('FAIL')
        time.sleep(5)

    def targeted_part_pumb(self):

        self.element_is_visible(Locators.PRODUCT_CARD).click()
        self.element_is_visible(Locators.BUY_ON_STORE_BUTTON).click()
        self.element_is_visible(Locators.CART).click()
        self.element_is_visible(Locators.CHOOSE_TARGETED_DELIVERY).click()
        self.element_is_visible(Locators.STREET).send_keys(OVL.street)
        self.element_is_visible(Locators.HOUSE).send_keys(OVL.house)
        self.element_is_visible(Locators.FLAT).send_keys(OVL.flat)
        self.element_is_visible(Locators.FLOR).send_keys(OVL.flor)
        self.element_is_visible(Locators.CHOOSE_PAYMENT_PART).click()
        self.element_is_visible(Locators.CHOOSE_PART_PUMB).click()
        self.element_is_visible(Locators.PHONE).send_keys(OVL.phone)
        self.element_is_visible(Locators.FIRST_NAME).send_keys(OVL.first_name)
        self.element_is_visible(Locators.SECOND_NAME).send_keys(OVL.second_name)
        self.element_is_visible(Locators.THIRD_NAME).send_keys(OVL.third_name)
        self.element_is_visible(Locators.COMMENTS).send_keys(OVL.comments)
        self.element_is_visible(Locators.DONT_CALL).click()
        self.element_is_visible(Locators.CHECKOUT).click()
        thp = self.element_is_visible(Locators.THP)
        if thp == thp:
            print('PASS')
        else:
            print('FAIL')
        time.sleep(5)

    def targeted_part_globus(self):

        self.element_is_visible(Locators.PRODUCT_CARD).click()
        self.element_is_visible(Locators.BUY_ON_STORE_BUTTON).click()
        self.element_is_visible(Locators.CART).click()
        self.element_is_visible(Locators.CHOOSE_TARGETED_DELIVERY).click()
        self.element_is_visible(Locators.STREET).send_keys(OVL.street)
        self.element_is_visible(Locators.HOUSE).send_keys(OVL.house)
        self.element_is_visible(Locators.FLAT).send_keys(OVL.flat)
        self.element_is_visible(Locators.FLOR).send_keys(OVL.flor)
        self.element_is_visible(Locators.CHOOSE_PAYMENT_PART).click()
        self.element_is_visible(Locators.CHOOSE_PART_GLOBUS).click()
        self.element_is_visible(Locators.PHONE).send_keys(OVL.phone)
        self.element_is_visible(Locators.FIRST_NAME).send_keys(OVL.first_name)
        self.element_is_visible(Locators.SECOND_NAME).send_keys(OVL.second_name)
        self.element_is_visible(Locators.THIRD_NAME).send_keys(OVL.third_name)
        self.element_is_visible(Locators.COMMENTS).send_keys(OVL.comments)
        self.element_is_visible(Locators.DONT_CALL).click()
        self.element_is_visible(Locators.CHECKOUT).click()
        globuspay = self.element_is_visible(Locators.THP)
        if globuspay != globuspay:
            print('PASS')
        else:
            print('FAIL')
        time.sleep(5)

    def targeted_part_otp(self):

        self.element_is_visible(Locators.PRODUCT_CARD).click()
        self.element_is_visible(Locators.BUY_ON_STORE_BUTTON).click()
        self.element_is_visible(Locators.CART).click()
        self.element_is_visible(Locators.CHOOSE_TARGETED_DELIVERY).click()
        self.element_is_visible(Locators.STREET).send_keys(OVL.street)
        self.element_is_visible(Locators.HOUSE).send_keys(OVL.house)
        self.element_is_visible(Locators.FLAT).send_keys(OVL.flat)
        self.element_is_visible(Locators.FLOR).send_keys(OVL.flor)
        self.element_is_visible(Locators.CHOOSE_PAYMENT_PART).click()
        self.element_is_visible(Locators.CHOOSE_PART_OTP).click()
        self.element_is_visible(Locators.PHONE).send_keys(OVL.phone)
        self.element_is_visible(Locators.FIRST_NAME).send_keys(OVL.first_name)
        self.element_is_visible(Locators.SECOND_NAME).send_keys(OVL.second_name)
        self.element_is_visible(Locators.THIRD_NAME).send_keys(OVL.third_name)
        self.element_is_visible(Locators.COMMENTS).send_keys(OVL.comments)
        self.element_is_visible(Locators.DONT_CALL).click()
        self.element_is_visible(Locators.CHECKOUT).click()
        thp = self.element_is_visible(Locators.THP)
        if thp == thp:
            print('PASS')
        else:
            print('FAIL')
        time.sleep(5)

    def targeted_part_sport(self):

        self.element_is_visible(Locators.PRODUCT_CARD).click()
        self.element_is_visible(Locators.BUY_ON_STORE_BUTTON).click()
        self.element_is_visible(Locators.CART).click()
        self.element_is_visible(Locators.CHOOSE_TARGETED_DELIVERY).click()
        self.element_is_visible(Locators.STREET).send_keys(OVL.street)
        self.element_is_visible(Locators.HOUSE).send_keys(OVL.house)
        self.element_is_visible(Locators.FLAT).send_keys(OVL.flat)
        self.element_is_visible(Locators.FLOR).send_keys(OVL.flor)
        self.element_is_visible(Locators.CHOOSE_PAYMENT_PART).click()
        self.element_is_visible(Locators.CHOOSE_PART_SPORT).click()
        self.element_is_visible(Locators.PHONE).send_keys(OVL.phone)
        self.element_is_visible(Locators.FIRST_NAME).send_keys(OVL.first_name)
        self.element_is_visible(Locators.SECOND_NAME).send_keys(OVL.second_name)
        self.element_is_visible(Locators.THIRD_NAME).send_keys(OVL.third_name)
        self.element_is_visible(Locators.COMMENTS).send_keys(OVL.comments)
        self.element_is_visible(Locators.DONT_CALL).click()
        self.element_is_visible(Locators.CHECKOUT).click()
        alert = self.element_is_visible(Locators.ALERT)
        if alert != alert:
            print('PASS')
        else:
            print('FAIL')
        time.sleep(5)

    def targeted_part_sense(self):

        self.element_is_visible(Locators.PRODUCT_CARD).click()
        self.element_is_visible(Locators.BUY_ON_STORE_BUTTON).click()
        self.element_is_visible(Locators.CART).click()
        self.element_is_visible(Locators.CHOOSE_TARGETED_DELIVERY).click()
        self.element_is_visible(Locators.STREET).send_keys(OVL.street)
        self.element_is_visible(Locators.HOUSE).send_keys(OVL.house)
        self.element_is_visible(Locators.FLAT).send_keys(OVL.flat)
        self.element_is_visible(Locators.FLOR).send_keys(OVL.flor)
        self.element_is_visible(Locators.CHOOSE_PAYMENT_PART).click()
        self.element_is_visible(Locators.CHOOSE_PART_SENSE).click()
        self.element_is_visible(Locators.NUM_CARD).send_keys(OVL.num_card)
        self.element_is_visible(Locators.PHONE).send_keys(OVL.phone)
        self.element_is_visible(Locators.FIRST_NAME).send_keys(OVL.first_name)
        self.element_is_visible(Locators.SECOND_NAME).send_keys(OVL.second_name)
        self.element_is_visible(Locators.THIRD_NAME).send_keys(OVL.third_name)
        self.element_is_visible(Locators.COMMENTS).send_keys(OVL.comments)
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

        self.element_is_visible(Locators.PRODUCT_CARD).click()
        self.element_is_visible(Locators.BUY_ON_STORE_BUTTON).click()
        self.element_is_visible(Locators.CART).click()
        self.element_is_visible(Locators.CHOOSE_NEW_POST_OFFICE).click()
        self.element_is_visible(Locators.CHOOSE_STORE_NEW_POST).click()
        self.element_is_visible(Locators.CHOOSE_PAYMENT_CASH).click()
        self.element_is_visible(Locators.PHONE).send_keys(OVL.phone)
        self.element_is_visible(Locators.FIRST_NAME).send_keys(OVL.first_name)
        self.element_is_visible(Locators.SECOND_NAME).send_keys(OVL.second_name)
        self.element_is_visible(Locators.THIRD_NAME).send_keys(OVL.third_name)
        self.element_is_visible(Locators.COMMENTS).send_keys(OVL.comments)
        self.element_is_visible(Locators.DONT_CALL).click()
        self.element_is_visible(Locators.CHECKOUT).click()
        thp = self.element_is_visible(Locators.THP)
        if thp == thp:
            print('PASS')
        else:
            print('FAIL')
        time.sleep(5)

    def new_post_privat24(self):

        self.element_is_visible(Locators.PRODUCT_CARD).click()
        self.element_is_visible(Locators.BUY_ON_STORE_BUTTON).click()
        self.element_is_visible(Locators.CART).click()
        self.element_is_visible(Locators.CHOOSE_NEW_POST_OFFICE).click()
        self.element_is_visible(Locators.CHOOSE_STORE_NEW_POST).click()
        self.element_is_visible(Locators.CHOOSE_PAYMENT_PRIVA24).click()
        self.element_is_visible(Locators.PHONE).send_keys(OVL.phone)
        self.element_is_visible(Locators.FIRST_NAME).send_keys(OVL.first_name)
        self.element_is_visible(Locators.SECOND_NAME).send_keys(OVL.second_name)
        self.element_is_visible(Locators.THIRD_NAME).send_keys(OVL.third_name)
        self.element_is_visible(Locators.COMMENTS).send_keys(OVL.comments)
        self.element_is_visible(Locators.DONT_CALL).click()
        self.element_is_visible(Locators.CHECKOUT).click()
        privat24pay = self.element_is_visible(Locators.PRIVAT24PAY)
        if privat24pay == privat24pay:
            print('PASS')
        else:
            print('FAIL')
        time.sleep(5)

    def new_post_googlepay(self):

        self.element_is_visible(Locators.PRODUCT_CARD).click()
        self.element_is_visible(Locators.BUY_ON_STORE_BUTTON).click()
        self.element_is_visible(Locators.CART).click()
        self.element_is_visible(Locators.CHOOSE_NEW_POST_OFFICE).click()
        self.element_is_visible(Locators.CHOOSE_STORE_NEW_POST).click()
        self.element_is_visible(Locators.CHOOSE_PAYMENT_GOOGLEPAY).click()
        self.element_is_visible(Locators.PHONE).send_keys(OVL.phone)
        self.element_is_visible(Locators.FIRST_NAME).send_keys(OVL.first_name)
        self.element_is_visible(Locators.SECOND_NAME).send_keys(OVL.second_name)
        self.element_is_visible(Locators.THIRD_NAME).send_keys(OVL.third_name)
        self.element_is_visible(Locators.COMMENTS).send_keys(OVL.comments)
        self.element_is_visible(Locators.DONT_CALL).click()
        googlepay = self.element_is_visible(Locators.CHECKOUT_GOOGLEPAY)
        if googlepay == googlepay:
            print('PASS')
        else:
            print('FAIL')
        time.sleep(5)

    def new_post_anycards(self):

        self.element_is_visible(Locators.PRODUCT_CARD).click()
        self.element_is_visible(Locators.BUY_ON_STORE_BUTTON).click()
        self.element_is_visible(Locators.CART).click()
        self.element_is_visible(Locators.CHOOSE_NEW_POST_OFFICE).click()
        self.element_is_visible(Locators.CHOOSE_STORE_NEW_POST).click()
        self.element_is_visible(Locators.CHOOSE_PAYMENT_ANY_CARDS).click()
        self.element_is_visible(Locators.PHONE).send_keys(OVL.phone)
        self.element_is_visible(Locators.FIRST_NAME).send_keys(OVL.first_name)
        self.element_is_visible(Locators.SECOND_NAME).send_keys(OVL.second_name)
        self.element_is_visible(Locators.THIRD_NAME).send_keys(OVL.third_name)
        self.element_is_visible(Locators.COMMENTS).send_keys(OVL.comments)
        self.element_is_visible(Locators.DONT_CALL).click()
        self.element_is_visible(Locators.CHECKOUT).click()
        ipay = self.element_is_visible(Locators.IPAY)
        if ipay == ipay:
            print('PASS')
        else:
            print('FAIL')
        time.sleep(5)

    def new_post_part_super(self):

        self.element_is_visible(Locators.PRODUCT_CARD).click()
        self.element_is_visible(Locators.BUY_ON_STORE_BUTTON).click()
        self.element_is_visible(Locators.CART).click()
        self.element_is_visible(Locators.CHOOSE_NEW_POST_OFFICE).click()
        self.element_is_visible(Locators.CHOOSE_STORE_NEW_POST).click()
        self.element_is_visible(Locators.CHOOSE_PAYMENT_PART).click()
        self.element_is_visible(Locators.CHOOSE_PART_SUPER).click()
        self.element_is_visible(Locators.IPN).send_keys(OVL.ipn)
        self.element_is_visible(Locators.PHONE).send_keys(OVL.phone)
        self.element_is_visible(Locators.FIRST_NAME).send_keys(OVL.first_name)
        self.element_is_visible(Locators.SECOND_NAME).send_keys(OVL.second_name)
        self.element_is_visible(Locators.THIRD_NAME).send_keys(OVL.third_name)
        self.element_is_visible(Locators.COMMENTS).send_keys(OVL.comments)
        self.element_is_visible(Locators.DONT_CALL).click()
        self.element_is_visible(Locators.CHECKOUT).click()
        thp = self.element_is_visible(Locators.THP)
        if thp == thp:
            print('PASS')
        else:
            print('FAIL')
        time.sleep(5)

    def new_post_part_privat(self):

        self.element_is_visible(Locators.PRODUCT_CARD).click()
        self.element_is_visible(Locators.BUY_ON_STORE_BUTTON).click()
        self.element_is_visible(Locators.CART).click()
        self.element_is_visible(Locators.CHOOSE_NEW_POST_OFFICE).click()
        self.element_is_visible(Locators.CHOOSE_STORE_NEW_POST).click()
        self.element_is_visible(Locators.CHOOSE_PAYMENT_PART).click()
        self.element_is_visible(Locators.CHOOSE_PART_PRIVAT).click()
        self.element_is_visible(Locators.PHONE).send_keys(OVL.phone)
        self.element_is_visible(Locators.FIRST_NAME).send_keys(OVL.first_name)
        self.element_is_visible(Locators.SECOND_NAME).send_keys(OVL.second_name)
        self.element_is_visible(Locators.THIRD_NAME).send_keys(OVL.third_name)
        self.element_is_visible(Locators.COMMENTS).send_keys(OVL.comments)
        self.element_is_visible(Locators.DONT_CALL).click()
        self.element_is_visible(Locators.CHECKOUT).click()
        thp = self.element_is_visible(Locators.THP)
        if thp == thp:
            print('PASS')
        else:
            print('FAIL')
        time.sleep(5)

    def new_post_part_mono(self):

        self.element_is_visible(Locators.PRODUCT_CARD).click()
        self.element_is_visible(Locators.BUY_ON_STORE_BUTTON).click()
        self.element_is_visible(Locators.CART).click()
        self.element_is_visible(Locators.CHOOSE_NEW_POST_OFFICE).click()
        self.element_is_visible(Locators.CHOOSE_STORE_NEW_POST).click()
        self.element_is_visible(Locators.CHOOSE_PAYMENT_PART).click()
        self.element_is_visible(Locators.CHOOSE_PART_MONO).click()
        self.element_is_visible(Locators.PHONE).send_keys(OVL.phone)
        self.element_is_visible(Locators.FIRST_NAME).send_keys(OVL.first_name)
        self.element_is_visible(Locators.SECOND_NAME).send_keys(OVL.second_name)
        self.element_is_visible(Locators.THIRD_NAME).send_keys(OVL.third_name)
        self.element_is_visible(Locators.EMAIL).send_keys(OVL.email)
        self.element_is_visible(Locators.COMMENTS).send_keys(OVL.comments)
        self.element_is_visible(Locators.DONT_CALL).click()
        self.element_is_visible(Locators.CHECKOUT).click()
        monopay = self.element_is_visible(Locators.MONOPAY)
        if monopay == monopay:
            print('PASS')
        else:
            print('FAIL')
        time.sleep(5)

    def new_post_part_oschad(self):

        self.element_is_visible(Locators.PRODUCT_CARD).click()
        self.element_is_visible(Locators.BUY_ON_STORE_BUTTON).click()
        self.element_is_visible(Locators.CART).click()
        self.element_is_visible(Locators.CHOOSE_NEW_POST_OFFICE).click()
        self.element_is_visible(Locators.CHOOSE_STORE_NEW_POST).click()
        self.element_is_visible(Locators.CHOOSE_PAYMENT_PART).click()
        self.element_is_visible(Locators.CHOOSE_PART_OSCHAD).click()
        self.element_is_visible(Locators.PHONE).send_keys(OVL.phone)
        self.element_is_visible(Locators.FIRST_NAME).send_keys(OVL.first_name)
        self.element_is_visible(Locators.SECOND_NAME).send_keys(OVL.second_name)
        self.element_is_visible(Locators.THIRD_NAME).send_keys(OVL.third_name)
        self.element_is_visible(Locators.COMMENTS).send_keys(OVL.comments)
        self.element_is_visible(Locators.DONT_CALL).click()
        self.element_is_visible(Locators.CHECKOUT).click()
        thp = self.element_is_visible(Locators.THP)
        if thp == thp:
            print('PASS')
        else:
            print('FAIL')
        time.sleep(5)

    def new_post_part_abank(self):

        self.element_is_visible(Locators.PRODUCT_CARD).click()
        self.element_is_visible(Locators.BUY_ON_STORE_BUTTON).click()
        self.element_is_visible(Locators.CART).click()
        self.element_is_visible(Locators.CHOOSE_NEW_POST_OFFICE).click()
        self.element_is_visible(Locators.CHOOSE_STORE_NEW_POST).click()
        self.element_is_visible(Locators.CHOOSE_PAYMENT_PART).click()
        self.element_is_visible(Locators.CHOOSE_PART_ABANK).click()
        self.element_is_visible(Locators.PHONE).send_keys(OVL.phone)
        self.element_is_visible(Locators.FIRST_NAME).send_keys(OVL.first_name)
        self.element_is_visible(Locators.SECOND_NAME).send_keys(OVL.second_name)
        self.element_is_visible(Locators.THIRD_NAME).send_keys(OVL.third_name)
        self.element_is_visible(Locators.COMMENTS).send_keys(OVL.comments)
        self.element_is_visible(Locators.DONT_CALL).click()
        self.element_is_visible(Locators.CHECKOUT).click()
        alert = self.element_is_visible(Locators.ALERT)
        if alert != alert:
            print('PASS')
        else:
            print('FAIL')
        time.sleep(5)

    def new_post_part_punb(self):

        self.element_is_visible(Locators.PRODUCT_CARD).click()
        self.element_is_visible(Locators.BUY_ON_STORE_BUTTON).click()
        self.element_is_visible(Locators.CART).click()
        self.element_is_visible(Locators.CHOOSE_NEW_POST_OFFICE).click()
        self.element_is_visible(Locators.CHOOSE_STORE_NEW_POST).click()
        self.element_is_visible(Locators.CHOOSE_PAYMENT_PART).click()
        self.element_is_visible(Locators.CHOOSE_PART_PUMB).click()
        self.element_is_visible(Locators.PHONE).send_keys(OVL.phone)
        self.element_is_visible(Locators.FIRST_NAME).send_keys(OVL.first_name)
        self.element_is_visible(Locators.SECOND_NAME).send_keys(OVL.second_name)
        self.element_is_visible(Locators.THIRD_NAME).send_keys(OVL.third_name)
        self.element_is_visible(Locators.COMMENTS).send_keys(OVL.comments)
        self.element_is_visible(Locators.DONT_CALL).click()
        self.element_is_visible(Locators.CHECKOUT).click()
        thp = self.element_is_visible(Locators.THP)
        if thp == thp:
            print('PASS')
        else:
            print('FAIL')
        time.sleep(5)

    def new_post_part_globus(self):

        self.element_is_visible(Locators.PRODUCT_CARD).click()
        self.element_is_visible(Locators.BUY_ON_STORE_BUTTON).click()
        self.element_is_visible(Locators.CART).click()
        self.element_is_visible(Locators.CHOOSE_NEW_POST_OFFICE).click()
        self.element_is_visible(Locators.CHOOSE_STORE_NEW_POST).click()
        self.element_is_visible(Locators.CHOOSE_PAYMENT_PART).click()
        self.element_is_visible(Locators.CHOOSE_PART_GLOBUS).click()
        self.element_is_visible(Locators.PHONE).send_keys(OVL.phone)
        self.element_is_visible(Locators.FIRST_NAME).send_keys(OVL.first_name)
        self.element_is_visible(Locators.SECOND_NAME).send_keys(OVL.second_name)
        self.element_is_visible(Locators.THIRD_NAME).send_keys(OVL.third_name)
        self.element_is_visible(Locators.COMMENTS).send_keys(OVL.comments)
        self.element_is_visible(Locators.DONT_CALL).click()
        self.element_is_visible(Locators.CHECKOUT).click()
        globuspay = self.element_is_visible(Locators.THP)
        if globuspay != globuspay:
            print('PASS')
        else:
            print('FAIL')
        time.sleep(5)

    def new_post_part_otp(self):

        self.element_is_visible(Locators.PRODUCT_CARD).click()
        self.element_is_visible(Locators.BUY_ON_STORE_BUTTON).click()
        self.element_is_visible(Locators.CART).click()
        self.element_is_visible(Locators.CHOOSE_NEW_POST_OFFICE).click()
        self.element_is_visible(Locators.CHOOSE_STORE_NEW_POST).click()
        self.element_is_visible(Locators.CHOOSE_PAYMENT_PART).click()
        self.element_is_visible(Locators.CHOOSE_PART_OTP).click()
        self.element_is_visible(Locators.PHONE).send_keys(OVL.phone)
        self.element_is_visible(Locators.FIRST_NAME).send_keys(OVL.first_name)
        self.element_is_visible(Locators.SECOND_NAME).send_keys(OVL.second_name)
        self.element_is_visible(Locators.THIRD_NAME).send_keys(OVL.third_name)
        self.element_is_visible(Locators.COMMENTS).send_keys(OVL.comments)
        self.element_is_visible(Locators.DONT_CALL).click()
        self.element_is_visible(Locators.CHECKOUT).click()
        thp = self.element_is_visible(Locators.THP)
        if thp == thp:
            print('PASS')
        else:
            print('FAIL')
        time.sleep(5)

    def new_post_part_sport(self):

        self.element_is_visible(Locators.PRODUCT_CARD).click()
        self.element_is_visible(Locators.BUY_ON_STORE_BUTTON).click()
        self.element_is_visible(Locators.CART).click()
        self.element_is_visible(Locators.CHOOSE_NEW_POST_OFFICE).click()
        self.element_is_visible(Locators.CHOOSE_STORE_NEW_POST).click()
        self.element_is_visible(Locators.CHOOSE_PAYMENT_PART).click()
        self.element_is_visible(Locators.CHOOSE_PART_SPORT).click()
        self.element_is_visible(Locators.PHONE).send_keys(OVL.phone)
        self.element_is_visible(Locators.FIRST_NAME).send_keys(OVL.first_name)
        self.element_is_visible(Locators.SECOND_NAME).send_keys(OVL.second_name)
        self.element_is_visible(Locators.THIRD_NAME).send_keys(OVL.third_name)
        self.element_is_visible(Locators.COMMENTS).send_keys(OVL.comments)
        self.element_is_visible(Locators.DONT_CALL).click()
        self.element_is_visible(Locators.CHECKOUT).click()
        alert = self.element_is_visible(Locators.ALERT)
        if alert != alert:
            print('PASS')
        else:
            print('FAIL')
        time.sleep(5)

    def new_post_part_sense(self):

        self.element_is_visible(Locators.PRODUCT_CARD).click()
        self.element_is_visible(Locators.BUY_ON_STORE_BUTTON).click()
        self.element_is_visible(Locators.CART).click()
        self.element_is_visible(Locators.CHOOSE_NEW_POST_OFFICE).click()
        self.element_is_visible(Locators.CHOOSE_STORE_NEW_POST).click()
        self.element_is_visible(Locators.CHOOSE_PAYMENT_PART).click()
        self.element_is_visible(Locators.CHOOSE_PART_SENSE).click()
        self.element_is_visible(Locators.NUM_CARD).send_keys(OVL.num_card)
        self.element_is_visible(Locators.PHONE).send_keys(OVL.phone)
        self.element_is_visible(Locators.FIRST_NAME).send_keys(OVL.first_name)
        self.element_is_visible(Locators.SECOND_NAME).send_keys(OVL.second_name)
        self.element_is_visible(Locators.THIRD_NAME).send_keys(OVL.third_name)
        self.element_is_visible(Locators.COMMENTS).send_keys(OVL.comments)
        self.element_is_visible(Locators.DONT_CALL).click()
        self.element_is_visible(Locators.CHECKOUT).click()
        alert = self.element_is_visible(Locators.ALERT)
        if alert != alert:
            print('PASS')
        else:
            print('FAIL')
        time.sleep(5)

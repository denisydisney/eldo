import time
from selenium.webdriver import Keys
from pages.base_page import BasePage
from locatros.search_variables import SearchVariablesLocators as SVL
from locatros.search_page_locators import SearchPageLocators as Locators


class Search(BasePage):
    def search_product(self):

        search_p = self.element_is_visible(Locators.INPUT_SEARCH)
        search_p.send_keys(SVL.product_name)
        search_p.send_keys(Keys.RETURN)
        time.sleep(5)

    def search_page_check(self):
        search_word = self.element_is_present(Locators.SEARCH_PEGE_TITLE)
        full_text = search_word.text
        words = full_text.split()
        second_word = words[2]

        if second_word == SVL.product_name:
            print(f'PASS')
            print(f'Слово поиска {SVL.product_name}')
            print(f'Слово тайтла {second_word}')
        else:
            print('FAIL')

    def search_show_all(self):

        self.element_is_visible(Locators.INPUT_SEARCH).send_keys(SVL.product_name)
        self.element_is_visible(Locators.SHOW_ALL).click()
        time.sleep(5)

    def search_choose_product(self):
        self.element_is_visible(Locators.INPUT_SEARCH).send_keys(SVL.product_name)
        goods_id_1 = self.element_is_visible(Locators.GOODS_CODE)
        goods_id_1 = goods_id_1.text
        time.sleep(5)
        self.element_is_visible(Locators.GOODS_CODE).click()
        time.sleep(2)
        goods_id_2 = self.element_is_visible(Locators.GOODS_CODE)
        goods_id_2 = goods_id_2.text
        print(goods_id_2)
        if goods_id_1 == goods_id_2:
            print('PASS')
            print(f'id поиск {goods_id_1}')
            print(f'id товар {goods_id_2}')
        else:
            print('FAIL')

    def search_maybe_loock(self):
        self.element_is_visible(Locators.INPUT_SEARCH).send_keys(SVL.product_name)
        maybe_loock_word = self.element_is_visible(Locators.MAYBE_LOOCK)
        maybe_loock_word = maybe_loock_word.text
        self.element_is_visible(Locators.MAYBE_LOOCK).click()
        return maybe_loock_word

    def search_page_check_1(self):
        maybe_loock_word = self.search_maybe_loock()
        search_word = self.element_is_present(Locators.SEARCH_PEGE_TITLE)
        full_text = search_word.text
        words = full_text.split()
        second_word = words[2]
        if second_word == maybe_loock_word.upper():
            print(f'PASS')
            print(f'Слово поиска {maybe_loock_word}')
            print(f'Слово тайтла {second_word}')
        else:
            print('FAIL')

    def search_in_category(self):
        self.element_is_visible(Locators.INPUT_SEARCH).send_keys(SVL.product_name)
        category = self.element_is_visible(Locators.CATEGORY)
        full_text = category.text
        words = full_text.split()
        category = words[0]
        self.element_is_visible(Locators.CATEGORY).click()
        return category

    def search_page_check_2(self):
        category = self.search_in_category()
        category_word = self.element_is_visible(Locators.CATEGORY_TITLE)
        category_word = category_word.text
        if category_word == category.upper():
            print(f'PASS')
            print(f'Слово категории {category}')
            print(f'Слово тайтла {category_word}')
        else:
            print('FAIL')

    def search_krakozyabra(self):

        search_k = self.element_is_visible(Locators.INPUT_SEARCH)
        search_k.send_keys(SVL.krakozyabra)
        search_k.send_keys(Keys.RETURN)
        time.sleep(5)

    def search_page_check3(self):
        search_word = self.element_is_present(Locators.KRAKOZYABRA_TITLE)
        search_word = search_word.text
        if search_word == SVL.krakozyabra:
            print(f'PASS')
            print(f'Слово поиска {SVL.krakozyabra}')
            print(f'Слово тайтла {search_word}')
        else:
            print('FAIL')


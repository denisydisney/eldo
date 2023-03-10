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
        # self.element_is_visible(Locators.SEARCH_PEGE_TITLE)
        # if search_title == SVL.product_name:
        #     print('PASS')
        # else:
        #     print('FAIL')
        time.sleep(150)

    def search_page_check(self):
        search_word = self.element_is_visible(Locators.SEARCH_PEGE_TITLE)
        full_text = search_word.text
        words = full_text.split()
        second_word = words[2]
        #return second_word

        if second_word == SVL.product_name:
            print(f'PASS')
            print(f'Слово тайтла {second_word}')
            print(f'Слово поиска {SVL.product_name}')
        else:
            print('FAIL')
        return second_word

    def search_show_all(self):

        self.element_is_visible(Locators.INPUT_SEARCH).send_keys(SVL.product_name)
        self.element_is_visible(Locators.SHOW_ALL).click()
        title = self.element_is_visible(Locators.SEARCH_PEGE_TITLE)
        if title == title:
            print('PASS')
        else:
            print('FAIL')
        time.sleep(5)

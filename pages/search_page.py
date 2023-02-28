import time
from selenium.webdriver import Keys
from pages.base_page import BasePage
from locatros.search_variables import SearchVariablesLocators as SVL
from locatros.search_page_locators import SearchPageLocators as Locators


class Search(BasePage):
    def search_product(self):

        search = self.element_is_visible(Locators.INPUT_SEARCH)
        search.send_keys(SVL.product_name)
        search.send_keys(Keys.RETURN)
        title = self.elements_are_visible(Locators.SEARCH_PEGE_TITLE)
        if title == title:
            print('PASS')
        else:
            print('FAIL')
        time.sleep(5)

    def search_show_all(self):

        self.element_is_visible(Locators.INPUT_SEARCH).send_keys(SVL.product_name)
        self.element_is_visible(Locators.SHOW_ALL).click()
        title = self.element_is_visible(Locators.SEARCH_PEGE_TITLE)
        if title == title:
            print('PASS')
        else:
            print('FAIL')
        time.sleep(5)

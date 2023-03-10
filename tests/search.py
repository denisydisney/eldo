from pages.search_page import Search


class TestSearch:

    def test_search_product(self, driver):
        search_page = Search(driver, 'https://eldorado.ua/uk/')
        search_page.open()
        search_page.search_product()
        search_page.search_page_check()
        # print(search_page.search_page_check())

    def test_search_show_all(self, driver):
        search_page = Search(driver, 'https://eldorado.ua/uk/')
        search_page.open()
        search_page.search_show_all()

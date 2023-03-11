from pages.search_page import Search


class TestSearch:

    def test_search_product(self, driver):
        search_page = Search(driver, 'https://eldorado.ua/uk/')
        search_page.open()
        search_page.search_product()
        search_page.search_page_check()

    def test_search_show_all(self, driver):
        search_page = Search(driver, 'https://eldorado.ua/uk/')
        search_page.open()
        search_page.search_show_all()
        search_page.search_page_check()

    def test_search_choose_product(self, driver):
        search_page = Search(driver, 'https://eldorado.ua/uk/')
        search_page.open()
        search_page.search_choose_product()

    def test_search_maybe_loock(self, driver):
        search_page = Search(driver, 'https://eldorado.ua/uk/')
        search_page.open()
        search_page.search_maybe_loock()
        search_page.search_page_check_1()

    def test_search_in_category(self, driver):
        search_page = Search(driver, 'https://eldorado.ua/uk/')
        search_page.open()
        search_page.search_in_category()
        search_page.search_page_check_2()

    def test_search_krakozyabra(self, driver):
        search_page = Search(driver, 'https://eldorado.ua/uk/')
        search_page.open()
        search_page.search_krakozyabra()
        search_page.search_page_check3()

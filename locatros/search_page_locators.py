from selenium.webdriver.common.by import By


class SearchPageLocators:
    INPUT_SEARCH = (By.XPATH, "//input[@type='search']")
    SEARCH_PEGE_TITLE = (By.XPATH, "//h5[@class='ui-library-heading4-c1b7']")
    POP_GOODS = (By.XPATH, "//h6[contains(text(),'Популярні товари')]")
    PERHAPS_YOU_FINDING = (By.XPATH, "//h6[contains(text(),'Можливо ви шукали')]")
    SHOW_ALL = (By.XPATH, "//a[contains(text(),'Показати всі товари')]")
    CHOOSE_GOODS = (By.XPATH, f"//div[@color='black'][contains(text(),'За запитом  ')]")
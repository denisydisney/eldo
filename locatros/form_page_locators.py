from selenium.webdriver.common.by import By


class FormPageLocators:
    # Карточка товара
    PRODUCT_CARD = (By.XPATH, "//span[contains(text(),'Пральна машина ELENBERG FS 5100 W')]")
    BUY_ON_STORE_BUTTON = (By.XPATH, "//*[.='Купити у кредит']")

    # Корзина
    CART = (By.CSS_SELECTOR, "a[class = 'continue-button']")
    PREVIEW_CART = (By.CSS_SELECTOR, "button[class*=checkout-button]")

    # Способ доставки
    CHOOSE_PICK_UP_FROM_STORE = (By.CSS_SELECTOR, "label[for='000000003']")
    CHOOSE_TARGETED_DELIVERY = (By.XPATH, "//label[@for='000000006']")
    CHOOSE_NEW_POST_OFFICE = (By.CSS_SELECTOR, "label[for='000000010']")

    # Отделение/магазин
    CHOOSE_STORE_PICK_UP = (By.CSS_SELECTOR, "div[class*=multimap-delivery-address]")
    CHOOSE_STORE_NEW_POST = (By.CSS_SELECTOR, "div[class*=multimap-delivery-address]")

    # Данные адресной доставки
    STREET = (By.XPATH, "//input[@placeholder='Назва вашої вулиці']")
    HOUSE = (By.XPATH, "//input[@placeholder='№ Дому']")
    FLAT = (By.XPATH, "//input[@placeholder='№ Квартири']")
    FLOR = (By.XPATH, "//input[@placeholder='№ Поверху']")

    # Способ оплаты
    CHOOSE_PAYMENT = (By.XPATH, "//label[@for = 'payment-type-000000001']")

    # Контактные данные
    PHONE = (By.XPATH, "//input[@name = 'phone']")
    FIRST_NAME = (By.XPATH, "//input[@name = 'name']")
    SECOND_NAME = (By.XPATH, "//input[@name = 'surname']")
    THIRD_NAME = (By.XPATH, "//input[@name = 'patronymic']")
    COMMENTS = (By.XPATH, "//textarea[@name = 'comment']")
    DONT_CALL = (By.XPATH, "//label[@for = 'called-for-client']")

    # Создание заказа
    CHECKOUT = (By.XPATH, "//button[@type = 'submit']")





    # PA = (By.CSS_SELECTOR, "[class='ui-library-action-80bf ui-library-actionLink-ec77 ui-library-buttonRadiusDefault-be7f #e1e6ee BottomHeaderLinestyled__IconContainerDiv-sc-i5edj7-7 fKVLpI']")

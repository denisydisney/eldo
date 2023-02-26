from selenium.webdriver.common.by import By


class AllPageLocators:
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
    CHOOSE_PAYMENT_CASH = (By.XPATH, "//label[@for = 'payment-type-000000001']")
    CHOOSE_PAYMENT_PRIVA24 = (By.XPATH, "//label[@for='payment-type-000000490']")
    CHOOSE_PAYMENT_GOOGLEPAY = (By.XPATH, "//label[@for = 'payment-type-000000492']")
    CHOOSE_PAYMENT_ANY_CARDS = (By.XPATH, "//label[@for = 'payment-type-000000493']")
    CHOOSE_PAYMENT_PART = (By.XPATH, "//label[@for='payment-type-credit']")

    # Виды оплат частями
    CHOOSE_PART_SUPER = (By.XPATH, "//div[@class='bank bank__label'][contains(text(),'СУПЕР РОЗСТРОЧКА!')]")
    IPN = (By.XPATH, "//input[@placeholder='Введіть Ваш ІПН']")
    CHOOSE_PART_PRIVAT = (By.XPATH, "//div[@class='bank bank__label'][contains(text(),'ПриватБанк')]")
    CHOOSE_PART_MONO = (By.XPATH, "//div[@class='bank bank__label'][normalize-space()='Monobank']")
    CHOOSE_PART_OSCHAD = (By.XPATH, "//div[contains(text(),'«Оплата частинами» від ОщадБанк')]")
    CHOOSE_PART_ABANK = (By.XPATH, "//div[@class='bank bank__label'][contains(text(),'А банк')]")
    CHOOSE_PART_PUMB = (By.XPATH, "//div[contains(text(),'Пумб')]")
    CHOOSE_PART_GLOBUS = (By.XPATH, "//div[contains(text(),'Плати частинами GlobusPlus (Глобус Банк)')]")
    CHOOSE_PART_OTP = (By.XPATH, "//div[contains(text(),'Плати частинами \"Скибочка\" від ОТР Банк')]")
    CHOOSE_PART_SPORT = (By.XPATH, "//div[contains(text(),'Sportbank')]")
    CHOOSE_PART_SENSE = (By.XPATH, "//div[@class='bank bank__label'][normalize-space()='Sense Bank']")
    NUM_CARD = (By.XPATH, "//input[@placeholder='Останні 4 цифри платіжної картки']")

    # Контактные данные
    PHONE = (By.XPATH, "//input[@name = 'phone']")
    FIRST_NAME = (By.XPATH, "//input[@name = 'name']")
    SECOND_NAME = (By.XPATH, "//input[@name = 'surname']")
    THIRD_NAME = (By.XPATH, "//input[@name = 'patronymic']")
    EMAIL = (By.XPATH, "//input[@placeholder='Напишіть ваш Email']")
    COMMENTS = (By.XPATH, "//textarea[@name = 'comment']")
    DONT_CALL = (By.XPATH, "//label[@for = 'called-for-client']")

    # Создание заказа
    CHECKOUT = (By.XPATH, "//button[@type = 'submit']")
    CHECKOUT_GOOGLEPAY = (By.XPATH, "//div[contains(@class,'gpay-card-info-placeholder-container')]")

    # Страница благодарности
    THP = (By.XPATH, '//*[@id="page-footer-content-id"]/div/div/div/div[1]/div[1]')
    IPAY = (By.XPATH, "//div[@id='partner']")
    MONOPAY = (By.XPATH, "//img[@alt='monobank-logo']")
    GLOBUSPAY = (By.XPATH, "//img[@alt='globus-logo']")
    PRIVAT24PAY = (By.XPATH, "//div[@class='container']")

    # Пуши
    ALERT = (By.XPATH, "//div[@role='alert']")

    # Авторизация
    PC_BATTON = (By.XPATH, "//div[contains(text(),'Кабінет')]")
    PHONE_AUTH = (By.XPATH, "//input[@placeholder='380']")
    SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']")
    PASWORD_AUTH = (By.XPATH, "//input[@placeholder='Введіть пароль для входу']")
    SHOW_PASWORD = (By.XPATH, "//label[@for='showPassword']")
    PC_PAGE = (By.XPATH, "//div[@class='contacts-container bottom-tier']")
    ERROR_TEXT = (By.XPATH, "//span[@class='new-not-require-input-error-text']")
    RECAPTCHA = (By.XPATH, "//iframe[@title='reCAPTCHA']")

    # Регистрация
    REG_FIRST_NAME = (By.XPATH, "//span[contains(text(),'Ім')]")
    REG_LAST_NAME = (By.XPATH, "//span[contains(text(),'Прізвище')]")
    REG_EMAIL = (By.XPATH, "//span[contains(text(),'Пошта')]")

    # Поиск
    INPUT_SEARCH = (By.XPATH, "//input[@type='search']")
    SEARCH_PEGE_TITLE = (By.CSS_SELECTOR, ".ui-library-heading4-c1b7")
    POP_GOODS = (By.XPATH, "//h6[contains(text(),'Популярні товари')]")
    PERHAPS_YOU_FINDING = (By.XPATH, "//h6[contains(text(),'Можливо ви шукали')]")
    SHOW_ALL = (By.XPATH, "//a[contains(text(),'Показати всі товари')]")

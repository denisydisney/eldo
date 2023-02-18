from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyautogui
import pytest


link = 'https://eldorado.ua/uk/'
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(link)
time.sleep(6)

pyautogui.scroll(-20)
time.sleep(5)

product_card = browser.find_element(By.XPATH, "//span[contains(text(),'Пральна машина ELENBERG FS 5100 W')]").click()
time.sleep(9)
buy_on_store_button = browser.find_element(By.XPATH, "//*[.='Купити у кредит']").click()

cart = WebDriverWait(browser, 15).until(
EC.presence_of_element_located((By.CSS_SELECTOR, "a[class = 'continue-button']"))).click()

choose_delivery = WebDriverWait(browser, 15).until(
EC.presence_of_element_located((By.XPATH, "//label[@for='000000006']"))).click()

street = WebDriverWait(browser, 15).until(
EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Назва вашої вулиці']")))
street.send_keys('Кіото')

house = WebDriverWait(browser, 15).until(
EC.presence_of_element_located((By.XPATH, "//input[@placeholder='№ Дому']")))
house.send_keys('13')

flat = WebDriverWait(browser, 15).until(
EC.presence_of_element_located((By.XPATH, "//input[@placeholder='№ Квартири']")))
flat.send_keys('80')

flor = WebDriverWait(browser, 15).until(
EC.presence_of_element_located((By.XPATH, "//input[@placeholder='№ Поверху']")))
flor.send_keys('11')

choose_payment = browser.find_element(By.CSS_SELECTOR, "label[for='payment-type-000000001']").click()

phone = browser.find_element(By.XPATH, "//input[@name = 'phone']")
phone.send_keys('666666666')

first_name = browser.find_element(By.XPATH, "//input[@name = 'name']")
first_name.send_keys('Denys')

second_name = browser.find_element(By.XPATH, "//input[@name = 'surname']")
second_name.send_keys('Budkov')

third_name = browser.find_element(By.XPATH, "//input[@name = 'patronymic']")
third_name.send_keys('Vasylevych')

comments = browser.find_element(By.XPATH, "//textarea[@name = 'comment']")
comments.send_keys('Test QA')

dont_call = browser.find_element(By.XPATH, "//label[@for = 'called-for-client']").click()

checkout = browser.find_element(By.XPATH, "//button[@type = 'submit']").click()

time.sleep(10)
thp = WebDriverWait(browser, 15).until(
EC.presence_of_element_located((By.XPATH, '//*[@id="page-footer-content-id"]/div/div/div/div[1]/div[1]')))
time.sleep(10)
if thp == thp:
    print('Pass')
else:
    print('Fall')
browser.quit()
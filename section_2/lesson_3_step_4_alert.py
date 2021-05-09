import os
import time
import math

from selenium import webdriver


LINK = "http://suninjuly.github.io/alert_accept.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(LINK)

    # Редирект на расчетную страницу
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    alert = browser.switch_to.alert
    alert.accept()

    time.sleep(1)

    # Расчет значения
    x_element = browser.find_element_by_css_selector('#input_value')
    x = x_element.text
    y = calc(x)

    # Отправка ответов
    browser.find_element_by_css_selector('#answer').send_keys(y)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()

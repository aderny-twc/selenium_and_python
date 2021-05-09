import os
import time
import math

from selenium import webdriver


LINK = "http://suninjuly.github.io/redirect_accept.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(LINK)

    # Можно удалить анимацию
    # browser.execute_script("document.getElementsByTagName('button')[0].classList.remove('trollface');")

    # Редирект на расчетную страницу
    button = browser.find_element_by_css_selector("button.btn")
    browser.execute_script("document.getElementsByTagName('button')[0].classList.remove('trollface');")
    button.click()

    time.sleep(1)

    # Получение имени второй вкладки
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

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

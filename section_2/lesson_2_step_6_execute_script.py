from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/execute_script.html"  # Страница без поля
    browser = webdriver.Chrome()
    browser.get(link)

    # Расчет значения
    x_element = browser.find_element_by_css_selector('#input_value')
    x = x_element.text
    y = calc(x)

    # Скролл
    button = browser.find_element_by_css_selector("button.btn")
    browser.execute_script("window.scrollBy(0, 100);")

    # Отправка ответов
    browser.find_element_by_css_selector('#answer').send_keys(y)

    option1 = browser.find_element_by_css_selector("[for='robotCheckbox']")
    option1.click()

    option2 = browser.find_element_by_css_selector("[for='robotsRule']")
    option2.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(5)
    browser.quit()

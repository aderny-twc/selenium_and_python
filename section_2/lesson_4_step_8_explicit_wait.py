import os
import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


LINK = "http://suninjuly.github.io/explicit_wait2.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(LINK)

    # Ждем цену, перед нажатием на кнопку
    button = browser.find_element_by_id("book")
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    )
    button.click()

    # Решаем задание
    x = browser.find_element_by_id('input_value').text
    y = calc(x)
    input_field = browser.find_element_by_id('answer')
    input_field.send_keys(y)
    browser.find_element_by_css_selector('#solve').click()

finally:
    time.sleep(5)
    browser.quit()

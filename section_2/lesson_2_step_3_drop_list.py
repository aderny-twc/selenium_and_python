from selenium import webdriver
import time
import math

# LINK = 'https://suninjuly.github.io/selects1.html'
LINK = 'https://suninjuly.github.io/selects2.html'


def calc_sum(num1, num2):
    return num1 + num2


try:
    browser = webdriver.Chrome()
    browser.get(LINK)

    num1 = browser.find_element_by_id('num1').text
    num2 = browser.find_element_by_id('num2').text

    answer = calc_sum(int(num1), int(num2))
    print(answer)

    browser.find_element_by_tag_name("select").click()
    browser.find_element_by_css_selector(f"[value='{answer}']").click()

    browser.find_element_by_css_selector('button.btn').click()

finally:
    time.sleep(10)
    browser.quit()

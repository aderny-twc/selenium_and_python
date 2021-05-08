from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    treasure = browser.find_element_by_id('treasure')
    treasure_attribute = treasure.get_attribute('valuex')
    print('Chest value', treasure_attribute)
    assert treasure_attribute is not None, 'Value under treasure icon is not reachable'

    y = calc(treasure_attribute)

    browser.find_element_by_css_selector('#answer').send_keys(y)

    browser.find_element_by_id('robotCheckbox').click()

    browser.find_element_by_id('robotsRule').click()

    browser.find_element_by_css_selector('button.btn').click()

finally:
    time.sleep(10)
    browser.quit()

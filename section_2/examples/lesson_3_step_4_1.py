# получение ответа и автоматический его ввод на степике
from selenium import webdriver
import os
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/alert_accept.html')

button = browser.find_element_by_class_name('btn-primary').click()
browser.switch_to.alert.accept()

x = browser.find_element_by_id("input_value").text
y = calc(x)

browser.find_element_by_id('answer').send_keys(y)
browser.find_element_by_class_name('btn-primary').click()

alert = browser.switch_to.alert
alert_text = alert.text.split()
alert.accept()
answer = alert_text[-1]

browser.get('https://stepik.org/catalog?auth=login&language=ru')
time.sleep(5)

browser.find_element_by_id('id_login_email').send_keys('***')# здесь вводится e-mail
browser.find_element_by_id('id_login_password').send_keys('***')# здесь вводится пароль

browser.find_element_by_class_name('sign-form__btn').click()
time.sleep(3)
browser.get('https://stepik.org/lesson/184253/step/4?unit=158843')
time.sleep(3)

answer_input = browser.find_element_by_css_selector('textarea')
browser.execute_script("return arguments[0].scrollIntoView(true);", answer_input)
answer_input.send_keys(answer)

button = browser.find_element_by_class_name('submit-submission')
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
time.sleep(1)
button.click()


# Авторизация ВК
loginWithVk = True
browser.get('https://stepik.org/catalog?auth=login&language=ru')
time.sleep(5)
if loginWithVk:
    browser.find_element_by_css_selector('.btn.btn-block.btn-social.btn-vk').click()
    time.sleep(2)
    # ниже вводятся e-mail и пароль Вконтакте (много где можно использовать)
    browser.find_element_by_xpath('//input[@name="email"]').send_keys('')
    browser.find_element_by_xpath('//input[@name="pass"]').send_keys('')
    browser.find_element_by_xpath('//button[@type="submit"]').click()
else:
    browser.find_element_by_id('id_login_email').send_keys('***')# здесь вводится e-mail
    browser.find_element_by_id('id_login_password').send_keys('***')# здесь вводится пароль
    browser.find_element_by_class_name('sign-form__btn').click()
time.sleep(3)

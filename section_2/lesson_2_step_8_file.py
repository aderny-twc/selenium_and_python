import os
import time
from selenium import webdriver


current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'media\empty_file.txt')           # добавляем к этому пути имя файла


try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    fist_name = browser.find_element_by_css_selector('input[name="firstname"]')
    fist_name.send_keys("Ivan")
    last_name = browser.find_element_by_css_selector('input[name="lastname"]')
    last_name.send_keys('Ivanov')
    email = browser.find_element_by_css_selector('input[name="email"]')
    email.send_keys('mymail@mail.com')

    uploading_button = browser.find_element_by_id('file')
    uploading_button.send_keys(file_path)

    browser.find_element_by_css_selector('button.btn').click()


finally:
    time.sleep(5)
    browser.quit()

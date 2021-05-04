from selenium import webdriver
import time

try:
    # link = "http://suninjuly.github.io/registration1.html"  # Корректная страница
    link = "http://suninjuly.github.io/registration2.html"  # Страница без поля
    browser = webdriver.Chrome()
    browser.get(link)

    # Обязательные поля
    input1 = browser.find_element_by_css_selector('div.first_block .first')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector("div.first_block .second")
    input2.send_keys("Ivanov")
    input3 = browser.find_element_by_css_selector('div.first_block .third')
    input3.send_keys("mymail@email.com")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # ждем загрузки страницы
    time.sleep(1)

    # Ищем заголовок
    welcome_text = browser.find_element_by_tag_name("h1").text

    # Проверка успешного заголовка
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()

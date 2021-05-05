from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/simple_form_find_task.html')
button1 = browser.find_element_by_id('submit_button')
button2 = browser.find_element(By.ID, 'submit_button')

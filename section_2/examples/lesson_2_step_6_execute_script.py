import math

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://SunInJuly.github.io/execute_script.html')

x = int(browser.find_element(By.ID, 'input_value').text)

answer = browser.find_element(By.ID, 'answer')
browser.execute_script('return arguments[0].scrollIntoView(true);', answer)
answer.send_keys(str(math.log(abs(12*math.sin(x)))))

robotCheckbox = browser.find_element(By.ID, 'robotCheckbox')
browser.execute_script('return arguments[0].scrollIntoView(true);', robotCheckbox)
robotCheckbox.click()

robotsRule = browser.find_element(By.ID, 'robotsRule')
browser.execute_script('return arguments[0].scrollIntoView(true);', robotsRule)
robotsRule.click()

button = browser.find_element(By.TAG_NAME, 'button')
browser.execute_script('return arguments[0].scrollIntoView(true);', button)
button.click()

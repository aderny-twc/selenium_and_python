import pytest
import time
import math

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


LINKS = [
    'https://stepik.org/lesson/236895/step/1',
    'https://stepik.org/lesson/236896/step/1',
    'https://stepik.org/lesson/236897/step/1',
    'https://stepik.org/lesson/236898/step/1',
    'https://stepik.org/lesson/236899/step/1',
    'https://stepik.org/lesson/236903/step/1',
    'https://stepik.org/lesson/236904/step/1',
    'https://stepik.org/lesson/236905/step/1'
]


@pytest.mark.parametrize('link', LINKS)
def test_get_links_with_correct_answer(browser, link):
    answer = str(math.log(int(time.time())))
    browser.get(link)
    browser.find_element_by_class_name('ember-text-area').send_keys(answer)
    browser.find_element_by_class_name('submit-submission').click()

    result = WebDriverWait(browser, 7).until(
        EC.presence_of_element_located((By.CLASS_NAME, "smart-hints__hint"))
    ).text

    result = browser.find_element_by_class_name('smart-hints__hint').text
    assert result == 'Correct!', f'*** The result is actually equals {result}'

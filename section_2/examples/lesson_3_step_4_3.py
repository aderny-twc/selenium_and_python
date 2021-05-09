import math
import os
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


def print_answer(remote: webdriver.Remote):
    alert = remote.switch_to.alert
    ans = alert.text.split()[-1]
    print(ans)
    alert.accept()

    return ans


def stepik_auth(remote: webdriver.Remote):
    remote.get(auth_link)
    WebDriverWait(remote, 3).until(lambda x: x.find_element_by_name("login"))
    auth_elems = ("login", "password")

    for auth_elem in auth_elems:
        remote.find_element_by_name(auth_elem).send_keys(os.getenv(auth_elem))
    remote.find_element_by_class_name("sign-form__btn").click()
    WebDriverWait(
        remote,
        3).until(lambda x: x.find_element_by_class_name("navbar__profile-img"))


def stepik_send_answer(remote: webdriver.Remote, answer: str):
    remote.get("https://stepik.org/lesson/184253/step/4?unit=158843")
    WebDriverWait(remote,
                  3).until(lambda x: x.find_element_by_tag_name("textarea"))
    remote.find_element_by_tag_name("textarea").send_keys(answer)
    remote.find_element_by_class_name("submit-submission").click()
    WebDriverWait(remote, 3).until(lambda x: x.find_element_by_id("correct"))


link = "http://suninjuly.github.io/alert_accept.html"
auth_link = "https://stepik.org/catalog?auth=login"
browser = webdriver.Chrome()
browser.get(link)

try:
    browser.find_element_by_css_selector("[type = \"submit\"]").click()
    browser.switch_to.alert.accept()
    WebDriverWait(browser,
                  5).until(lambda x: x.find_element_by_id("input_value"))
    browser.find_element_by_id("answer").send_keys(
        calc(browser.find_element_by_id("input_value").text))
    browser.find_element_by_css_selector("[type = \"submit\"]").click()
    answer = print_answer(browser)
    stepik_auth(browser)
    stepik_send_answer(browser, answer)
finally:
    browser.quit()

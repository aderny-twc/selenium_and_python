from selenium import webdriver
import unittest
import time

class TestAbs(unittest.TestCase):
    def test_registrations_requireded_fields_1(self):
        try:
            browser = webdriver.Chrome()
            link = "http://suninjuly.github.io/registration1.html"
            browser.get(link)

            input1 = browser.find_element_by_css_selector(".first[required]")
            input1.send_keys("Ivan")
            input2 = browser.find_element_by_css_selector(".second[required]")
            input2.send_keys("Ivanov")
            input3 = browser.find_element_by_css_selector(".third[required]")
            input3.send_keys("ivanivan@mail.com")

            button = browser.find_element_by_css_selector("button.btn")
            button.click()

            time.sleep(1)

            welcome_text_elt = browser.find_element_by_tag_name("h1")
            welcome_text = welcome_text_elt.text
        finally:
            time.sleep(3)
            browser.quit()

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Should be - Congratulations! You have successfully registered!")

    def test_registrations_requireded_fields_2(self):
        try:
            browser = webdriver.Chrome()
            link = "http://suninjuly.github.io/registration2.html"
            browser.get(link)

            input1 = browser.find_element_by_css_selector(".first[required]")
            input1.send_keys("Ivan")
            input2 = browser.find_element_by_css_selector(".second[required]")
            input2.send_keys("Ivanov")
            input3 = browser.find_element_by_css_selector(".third[required]")
            input3.send_keys("ivanivan@mail.com")

            button = browser.find_element_by_css_selector("button.btn")
            button.click()

            time.sleep(1)

            welcome_text_elt = browser.find_element_by_tag_name("h1")

            welcome_text = welcome_text_elt.text
        finally:
            time.sleep(3)
            browser.quit()

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Should be - Congratulations! You have successfully registered!")

if __name__ == "__main__":
    unittest.main()

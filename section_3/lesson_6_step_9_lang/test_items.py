from selenium import webdriver
import time


LINK = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_button_add_to_cart(browser, link=LINK):
    """Checking for the "add to cart" button."""
    browser.get(link)
    # time.sleep(30.0)
    add_to_cart = browser.find_element_by_css_selector(".btn-add-to-basket")

    assert add_to_cart != None, '"Add to cart" button not found'

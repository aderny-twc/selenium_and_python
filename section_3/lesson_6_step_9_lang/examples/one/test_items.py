link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_add_to_basket_button_exist(browser):
    browser.get(link)

    add_to_basket_button = browser.find_elements_by_css_selector(".add-to-basket .btn-add-to-basket")

    assert len(add_to_basket_button) > 0, "Button Add To Basket NOT Exist!"

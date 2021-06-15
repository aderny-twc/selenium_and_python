import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    # Выбор браузера
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome/firefox")
    # Выбор языка
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: --language=<lang>")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser_language = request.config.getoption("language")
    browser = None

    if browser_name == "chrome":
        print("\nStarting chrome browser for tests...")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': browser_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nStarting firefox browser for tests...")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", browser_language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name not found")

    yield browser

    browser.quit()

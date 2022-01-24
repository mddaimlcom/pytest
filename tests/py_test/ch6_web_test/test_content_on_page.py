from ..helpers import EndavaPo as EN
from pathlib import Path

# module level variables
browser_args = {
    'executable_path': '~/WebDrivers/geckodriver',
    "cookies": '/tests/py_test/data_artifacts/endava_cookies.pkl',
    "domain_url": 'https://www.endava.com'
}

capabilities_page_text = ['TRANSACTION ADVISORY', 'ORGANISATIONAL OPTIMISATION', 'TELEMETRY & MONITORING', 'SMART DESK']
homepage_url = 'https://www.endava.com/'


# actual tests
def test_about_page(browser):
    browser_handler = EN.EndavaAboutPage(browser)
    browser_handler.nav(homepage_url)
    browser_handler.handle_cooki_question()  # on first run accept the cookies
    browser_handler.menu_button.click()
    browser_handler.about_btn.click()
    assert "WELCOME TO ENDAVA" in browser_handler.page_text


def test_contact_page(browser):
    browser_handler = EN.EndavaContactPage(browser)
    browser_handler.nav(homepage_url)
    browser_handler.menu_button.click()
    browser_handler.contact_btn.click()
    assert "CONTACT US" in browser_handler.page_text


def test_capabilities_page(browser):
    browser_handler = EN.EndavaCapabilitiestPage(browser)
    browser_handler.nav(homepage_url)
    browser_handler.menu_button.click()
    browser_handler.capabilities_btn.click()
    for text in capabilities_page_text:
        assert text in browser_handler.page_text

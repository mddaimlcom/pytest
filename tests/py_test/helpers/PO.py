from abc import ABC
from time import sleep
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *


class AbstractPage(ABC):

    _implicit_element_wait = 2

    _implicit_page_wait = 10

    def __init__(self, browser_object):
        self._browser = browser_object  # type: WebDriver
        self._browser.set_page_load_timeout(self._implicit_page_wait)
        self._browser.implicitly_wait(self._implicit_element_wait)
        self._browser.maximize_window()

    @property
    def browser(self) -> WebDriver:
        return self._browser

    @property
    def current_url(self):
        return self.browser.current_url

    @property
    def page_text(self):
        return self._browser.find_element(By.TAG_NAME, "body").text

    def find_by_xpath(self, *identifiers: str) -> WebElement:
        _el = None
        for id in identifiers:
            try:
                _el = self.browser.find_element(By.XPATH, id)
                return _el
            except Exception as ex:
                print(str(ex))
            finally:
                pass
        return _el

    def find_elements(self, *identifiers):
        """
    Get the list of elements that matched the respective xpath identifiers
        :param identifiers: str
        :return: list[WebElement]
        """
        elements = list()
        for id in identifiers:
            try:
                elements.extend(self.browser.find_elements(By.XPATH, id))
                return elements
            except Exception as ex:
                print(str(ex))
            finally:
                pass
        return elements



    def nav(self, url):
        self.browser.get(url)

    def wait_for_element(self, xpath_identifier):
        wait = WebDriverWait(self.browser, self._implicit_element_wait, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                                 ElementNotInteractableException, ElementClickInterceptedException,
                                                 NoSuchElementException, StaleElementReferenceException]
                             )

        try:
            elem = wait.until(EC.element_to_be_clickable((By.XPATH, xpath_identifier)))
        except TimeoutException:
            return None
        return elem

    def static_wait(self, t_unit=None):
        if t_unit:
            sleep(t_unit)
        else:
            sleep(self._implicit_element_wait)








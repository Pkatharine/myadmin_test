from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# from config import TIMEOUT

class Wrapper(object):
    """Webdriver wrapper"""

    def __init__(self, driver, default_timeout=10):
        self.driver = driver
        self.default_timeout = default_timeout

    def get_element(self, locator):
        """Returns all elements for the specific locator"""
        return self.driver.find_element(*locator)

    def get_elements(self, locator):
        """Returns all elements for the specific locator"""
        WebDriverWait(self.driver, self.default_timeout).until(EC.presence_of_all_elements_located(locator))
        return self.driver.find_elements(*locator)

    def find_element(self, locator, time=20):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=20):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

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

    def get_elements_by_text(self, locator):
            """Returns element with specific text for the specific locator"""
            WebDriverWait(self.driver, self.default_timeout).until(EC.element_to_be_clickable(locator[0]))
            elements = self.driver.find_elements(*locator[0])
            for element in elements:
                if element.text == locator[1]:
                    return element

    def click_element(self, locator, elem_number=0):
        """Clicks on the element with number elem_number"""
        WebDriverWait(self.driver, self.default_timeout,ignored_exceptions=ElementClickInterceptedException).\
        until(EC.element_to_be_clickable(locator))
        elements = self.get_elements(locator)
        elements[elem_number].click()

    def click_element_by_text(self, locator, text_value):
        """Clicks on the element with text attribute text_value"""
        WebDriverWait(self.driver, self.default_timeout, ignored_exceptions=StaleElementReferenceException).\
            until(EC.element_to_be_clickable(locator))
        elements = self.get_elements(locator)
        for element in elements:
            if element.text == text_value:
                element.click()

    def clear_element(self, locator):
        """Clears the element with the specific text_value"""
        WebDriverWait(self.driver, self.default_timeout).until(EC.presence_of_element_located(locator))
        self.get_element(locator).clear()

    def send_keys(self, locator, keys, text_value='default'):
        """Send keys to the element with the the specific text_value"""
        WebDriverWait(self.driver, self.default_timeout).until(EC.presence_of_element_located(locator))
        elements = self.get_elements(locator)
        if text_value == 'default':
            elements[0].send_keys(keys)
        else:
            for element in elements:
                if element.text == text_value:
                    element.send_keys(keys)

    def get_attr_value(self, locator, attr):
        """Get attribute value of the element"""
        WebDriverWait(self.driver, self.default_timeout)\
            .until(EC.element_to_be_clickable(locator))
        element = self.get_element(locator)
        return element.get_attribute(attr)

    def get_text_of_element(self, locator):
        """ Get text from element """
        WebDriverWait(self.driver, self.default_timeout).until(EC.visibility_of_element_located(locator))
        return self.get_element(locator).text

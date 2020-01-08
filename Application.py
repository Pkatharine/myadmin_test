from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# from PageObjects.LeftPanel import LeftPanel
import PageObjects.LeftPanel


class Application:

    def __init__(self, browser):
        self.browser = browser
        # self.driver = driver
        self.base_url = "http://localhost/phpmyadmin/"
        self.browser.get(self.base_url)
        self.left_panel = PageObjects.LeftPanel(self.browser)

    def find_element(self, locator, time=20):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=20):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    # def go_to_site(self):
    #     return

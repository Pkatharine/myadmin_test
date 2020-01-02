from selenium.webdriver.common.by import By

from PageObjects.BasePage import BasePage


class LeftPanelLocators:
    databases_list_left_panel = (By.XPATH, "//li[@class = 'database' or @class = 'last database']/a")


class LeftPanelTestData:
    db_names = ['information_schema', 'mysql', 'performance_schema', 'phpmyadmin', 'test']


class LeftPanel(BasePage):

    def get_list_of_databases(self):
        return [i.text for i in self.find_elements(LeftPanelLocators.databases_list_left_panel)]

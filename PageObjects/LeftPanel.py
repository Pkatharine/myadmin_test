from selenium.webdriver.common.by import By

from PageObjects.BasePage import BasePage


class LeftPanelLocators:
    databases_list_left_panel = (By.XPATH, "//li[@class = 'database' or @class = 'last database']/a")
    add_database_button = (By.CSS_SELECTOR, "#pma_navigation_tree_content a.hover_show_full")
    selected_db = (By.CSS_SELECTOR, "li.database.selected")

class LeftPanelTestData:
    db_names = ['information_schema', 'mysql', 'performance_schema', 'phpmyadmin', 'test']


class LeftPanel(BasePage):

    def get_list_of_databases(self):
        return [i.text for i in self.find_elements(LeftPanelLocators.databases_list_left_panel)]

    def click_add_database(self):
        return self.find_element(LeftPanelLocators.add_database_button).click()

    def get_name_of_selected_database(self):
        return self.find_element(LeftPanelLocators.selected_db).text




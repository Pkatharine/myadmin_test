from Application import Application
from selenium.webdriver.common.by import By


class ServerDatabaseLocators:
    db_name_input = (By.CSS_SELECTOR, "#text_create_db")
    db_submit_button = (By.CSS_SELECTOR, "#buttonGo")


class ServerDatabasePage(Application):

    def type_db_name(self, word):
        name_input = self.find_element(ServerDatabaseLocators.db_name_input)
        name_input.send_keys(word)

    def click_submit(self):
        return self.find_element(ServerDatabaseLocators.db_submit_button).click()

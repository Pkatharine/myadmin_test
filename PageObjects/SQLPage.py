from PageObjects.BasePage import BasePage
from selenium.webdriver.common.by import By


class SQLPageLocators:
    db_name_input = (By.CSS_SELECTOR, "'# CodeMirror-line '")
    db_submit_button = (By.CSS_SELECTOR, "'#buttonGo'")


class SQLPage(BasePage):

    def createDBQuery(self, word):
        name_input = self.find_element(SQLPageLocators.db_name_input).click()
        name_input.send_keys(word)

    def click_submit(self):
        return self.find_element(SQLPageLocators.db_submit_button).click()

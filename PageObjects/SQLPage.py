from selenium.webdriver.common.by import By




class SQLPageLocators:
    db_name_input = (By.CSS_SELECTOR, "'# CodeMirror-line '")
    db_submit_button = (By.CSS_SELECTOR, "'#buttonGo'")


class SQLPage():
    def __init__(self, browser):
        self.browser = browser

    def createDBQuery(self, word):
        name_input = self.browser.find_element(SQLPageLocators.db_name_input).click()
        name_input.send_keys(word)

    def click_submit(self):
        return self.browser.find_element(SQLPageLocators.db_submit_button).click()

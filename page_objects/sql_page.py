from selenium.webdriver.common.by import By




class SQLPageLocators:
    db_name_input = (By.XPATH, '/html/body/div[4]/form/div/fieldset/div[1]/div[1]/textarea')
    db_submit_button = (By.CSS_SELECTOR, "#button_submit_query")


class SQLPage():
    def __init__(self, browser):
        self.browser = browser

    def createDBQuery(self, word):
        self.browser.send_keys(SQLPageLocators.db_name_input, word)

    def click_submit(self):
        return self.browser.find_element(SQLPageLocators.db_submit_button).click()

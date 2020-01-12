from selenium.webdriver.common.by import By
 
class CreateTablePageLocators:
    table_name_input = (By.CSS_SELECTOR, "#create_table_form_minimal > fieldset:nth-child(1) > div:nth-child(4) > input[type=text]")
    go_button = (By.CSS_SELECTOR, "#create_table_form_minimal > fieldset.tblFooters > input[type=submit]")


class CreateTablePage():
    def __init__(self, browser):
        self.browser = browser

    def click_go(self):
        return self.browser.find_element(CreateTablePageLocators.go_button).click()
    
    def type_table_name(self, name):
        el = self.browser.find_element(CreateTablePageLocators.table_name_input)
        el.send_keys(name)

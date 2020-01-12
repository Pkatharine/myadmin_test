from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
 
class TableFillerPageLocators:
    first_input_column_length = (By.CSS_SELECTOR, "#field_0_3")
    first_input_column_name = (By.CSS_SELECTOR, "#field_0_1")
    table_name_picker = (By.CSS_SELECTOR, "#table_name_col_no > tbody > tr > td:nth-child(1) > input")

class TableFillerPage():
    def __init__(self, browser):
        self.browser = browser
    
    def get_value_of_table_name_picker(self):
        el = self.browser.get_attr_value(TableFillerPageLocators.table_name_picker, 'value')
        return el
    
    def type_first_column_definition(self, name, length):
        self.browser.send_keys(TableFillerPageLocators.first_input_column_name, name)
        self.browser.send_keys(TableFillerPageLocators.first_input_column_length, length)
        self.browser.send_keys(TableFillerPageLocators.first_input_column_length, Keys.RETURN)
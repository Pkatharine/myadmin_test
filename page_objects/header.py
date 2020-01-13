from selenium.webdriver.common.by import By


class HeaderNavigationLocators:
    databases_page = (By.CSS_SELECTOR, "server_databases.php")  # fix
    sql_page = (By.CSS_SELECTOR, '[title="SQL"]')
    server_status_page = (By.CSS_SELECTOR, "server_status.php")  # fix
    user_accounts_page = (By.CSS_SELECTOR, "server_privileges.php")  # fix


class HeaderNavigationPage():

    def __init__(self, browser):
        self.browser = browser

    def click_databases_page(self):
        self.browser.find_element(HeaderNavigationLocators.databases_page).click()

    def click_SQL_page(self):
        self.browser.find_element(HeaderNavigationLocators.sql_page).click()

    def click_status_page(self):
        self.browser.find_element(HeaderNavigationLocators.server_status_page).click()

    def click_user_accounts_page(self):
        self.browser.find_element(HeaderNavigationLocators.add_database_button).click()

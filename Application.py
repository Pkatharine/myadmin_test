from PageObjects.left_navigation_page import LeftNavigationPage
from PageObjects.SQL_page import SQLPage
from PageObjects.database_page import ServerDatabasePage
from PageObjects.create_table import CreateTablePage

"""Guide:
    Create page with methods
        include page here
    Create test use fixture "app"
        use 'self.browser = browser' in init
"""


class Application():

    def __init__(self, browser):
        self.browser = browser
        self.sqlPage = SQLPage(self.browser)
        self.left_panel = LeftNavigationPage(self.browser)
        self.server_db = ServerDatabasePage(self.browser)
        self.create_table_page = CreateTablePage(self.browser)
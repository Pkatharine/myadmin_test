from page_objects.left_navigation_page import LeftNavigationPage
from page_objects.sql_page import SQLPage
from page_objects.database_page import ServerDatabasePage
from page_objects.create_table import CreateTablePage
from page_objects.table_filler_page import TableFillerPage

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
        self.table_filler_page = TableFillerPage(self.browser)
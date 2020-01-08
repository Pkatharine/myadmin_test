from PageObjects.left_navigation_page import LeftNavigationPage
from PageObjects.database_page import ServerDatabasePage


class CreateDbTestHelper:
    def create_database(name, br):
        left_panel = LeftNavigationPage(br)
        left_panel.click_add_database()
        server_db = ServerDatabasePage(br)
        server_db.type_db_name(name)
        server_db.click_submit()

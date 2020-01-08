from PageObjects.LeftPanel import LeftPanel
from PageObjects.databasePage import ServerDatabasePage


class CreateDbTestHelper:
    def create_database(name, br):
        left_panel = LeftPanel(br)
        left_panel.go_to_site()
        left_panel.click_add_database()
        server_db = ServerDatabasePage(br)
        server_db.type_db_name(name)
        server_db.click_submit()

import time

from PageObjects.LeftPanel import LeftPanel
from PageObjects.ServerDatabasePage import ServerDatabasePage


def test_create_db_ui(browser):
    left_panel = LeftPanel(browser)
    left_panel.go_to_site()
    left_panel.click_add_database()
    server_db = ServerDatabasePage(browser)
    server_db.type_db_name("hey1")
    server_db.click_submit()
    assert "hey1" == left_panel.get_name_of_selected_database()

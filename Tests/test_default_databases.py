from PageObjects.LeftPanel import LeftPanel, LeftPanelTestData


def test_default_databases(browser):
    left_panel = LeftPanel(browser)
    left_panel.go_to_site()
    actual = left_panel.get_list_of_databases()
    expected = LeftPanelTestData.db_names
    for i in expected:
        assert i in actual

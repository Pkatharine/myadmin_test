from PageObjects.LeftPanel import LeftPanel, LeftPanelTestData


def test_default_databases(browser):
    actual = self.browser.get_list_of_databases()
    expected = LeftPanelTestData.db_names
    for i in expected:
        assert i in actual

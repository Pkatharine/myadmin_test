from PageObjects.LeftPanel import LeftPanelTestData


def test_default_databases(app):
    actual = app.left_panel.get_list_of_databases()
    expected = LeftPanelTestData.db_names
    for i in expected:
        assert i in actual

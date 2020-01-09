from TestHelpers.createDbUITestHelper import createDbUITestHelper as testHelper

def test_create_db_ui(app):
    testHelper.create_database(app, "111")
    assert "111" == app.left_panel.get_name_of_selected_database()

def test_create_table(app):
    testHelper.create_table(app, "table")



from test_helpers.createDbUITestHelper import createDbUITestHelper as testHelper

def test_create_db_ui(app):
    testHelper.create_database(app, "111")
    assert "111" == app.left_panel.get_name_of_selected_database()

def test_create_table(app):
    testHelper.create_table(app, "table")
    assert "table" == app.table_filler_page.get_value_of_table_name_picker()

def test_create_column(app):
    app.table_filler_page.type_first_column_definition("table", 255)
    

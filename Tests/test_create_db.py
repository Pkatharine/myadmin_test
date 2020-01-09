
def test_create_db_ui(app):
    app.left_panel.click_add_database()
    app.server_db.type_db_name("neeew")
    app.server_db.click_submit()
    assert "neeew" == app.left_panel.get_name_of_selected_database()
    

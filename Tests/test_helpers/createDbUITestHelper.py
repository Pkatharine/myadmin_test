class createDbUITestHelper:
    def create_database(app, name):
        app.left_panel.click_add_database()
        app.server_db.type_db_name(name)
        app.server_db.click_submit()

    def create_table(app, name):
        app.create_table_page.click_go()
        app.create_table_page.type_table_name(name)
        
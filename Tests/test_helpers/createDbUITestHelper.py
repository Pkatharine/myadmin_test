import allure


class createDbUITestHelper:
    def create_database(app, name):
        with allure.step("Click 'new' in the left panel"):
            app.left_panel.click_add_database()
        with allure.step("Type %s in input field to create database" %name):
            app.server_db.type_db_name(name)
        with allure.step("Click submit"):
            app.server_db.click_submit()

    def create_table(app, name):
        with allure.step("Type %s in input field to create table" %name):
            app.create_table_page.type_table_name(name)
        with allure.step("Click 'go'"):
            app.create_table_page.click_go()

import pytest
from test_helpers.createDbUITestHelper import createDbUITestHelper as testHelper
import allure


@allure.suite("Creating database cycle")
@allure.story("Creating database via UI")
@allure.severity(allure.severity_level.CRITICAL)
@allure.link("http://localhost/phpmyadmin/index.php?lang=en", name='click PhpMyAdmin')
def test_create_db_ui(app):
    with allure.step("Create new database:"):
        testHelper.create_database(app, "111")
    with allure.step("Verify that database was created successfully"):
        assert "111" == app.left_panel.get_name_of_selected_database()


@allure.suite('Creating database cycle')
@allure.story("Creating table via UI")
@allure.severity(allure.severity_level.CRITICAL)
@allure.link("http://localhost/phpmyadmin/index.php?lang=en", name='click PhpMyAdmin')
def test_create_table(app):
    with allure.step("Create new table:"):
        testHelper.create_table(app, "table")
    with allure.step("Verify that table was created successfully"):
        assert "table" == app.table_filler_page.get_value_of_table_name_picker()


@allure.suite('Creating database cycle')
@allure.story("Creating column via UI")
@allure.severity(allure.severity_level.CRITICAL)
@allure.link("http://localhost/phpmyadmin/index.php?lang=en", name='click PhpMyAdmin')
@pytest.mark.usefixtures('cleanup_db_delete')
def test_create_column(app):
    with allure.step("Create new column:"):
        app.table_filler_page.type_first_column_definition("table", 255)

import pytest
from test_helpers.createDbUITestHelper import createDbUITestHelper as testHelper
import allure


@allure.suite("Creating database cycle")
@allure.story("Creating database via UI")
@allure.severity(allure.severity_level.CRITICAL)
@allure.link("http://localhost/phpmyadmin/index.php?lang=en", name='click PhpMyAdmin')
def test_create_db_ui(app):
    testHelper.create_database(app, "111")
    assert "111" == app.left_panel.get_name_of_selected_database()


@allure.suite('Creating database cycle')
@allure.story("Creating table via UI")
@allure.severity(allure.severity_level.CRITICAL)
@allure.link("http://localhost/phpmyadmin/index.php?lang=en", name='click PhpMyAdmin')
def test_create_table(app):
    testHelper.create_table(app, "table")
    assert "table" == app.table_filler_page.get_value_of_table_name_picker()


@allure.suite('Creating database cycle')
@allure.story("Creating column via UI")
@allure.severity(allure.severity_level.CRITICAL)
@allure.link("http://localhost/phpmyadmin/index.php?lang=en", name='click PhpMyAdmin')
@pytest.mark.usefixtures('cleanup_db_delete')
def test_create_column(app):
    app.table_filler_page.type_first_column_definition("table", 255)

import allure
from page_objects.left_navigation_page import LeftPanelTestData


@allure.suite('Verify that default databases are present on home page')
@allure.severity(allure.severity_level.MINOR)
@allure.link("http://localhost/phpmyadmin/index.php?lang=en", name='PhpMyAdmin')
def test_default_databases(app):
    actual = app.left_panel.get_list_of_databases()
    expected = LeftPanelTestData.db_names
    with allure.step("Verify list of default db's"):
        for i in expected:
            assert i in actual

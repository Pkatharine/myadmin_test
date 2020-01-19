import time

import pytest

from page_objects.sql_page import SQLPage

@pytest.mark.xfail(condition=lambda: True, reason='this test is expecting failure')
def test_default_databases(useThis):
    sql_page = SQLPage(browser)
    # sql_page.go_to_site()
    sql_page.click_element('[title="SQL"]')
    sql_page.createDBQuery('CREATE DATABASE `test_table`')

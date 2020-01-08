import time

from PageObjects.SQL_page import SQLPage


def test_default_databases(useThis):
    sql_page = SQLPage(browser)
    # sql_page.go_to_site()
    sql_page.click_element('[title="SQL"]')
    sql_page.createDBQuery('CREATE DATABASE `test_table`')

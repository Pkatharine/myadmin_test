import time

from PageObjects.SQLPage import SQLPage


def test_default_databases(browser):
    sql_page = SQLPage(browser)
    # sql_page.go_to_site()
    sql_page.click_element('[title="SQL"]')
    sql_page.createDBQuery('CREATE DATABASE `test_table`')

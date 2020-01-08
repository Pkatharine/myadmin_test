import time

from PageObjects.SQLPage import SQLPage


def test_default_databases(browser):
    sql_page = SQLPage(browser)
    time.sleep(5)
    sql_page.click_element('#title="SQL"')
    sql_page.createDBQuery('CREATE DATABASE `test_table`')

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from Application import Application
from wrapper import Wrapper
from db import DbConnection


@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.get("http://localhost/phpmyadmin/index.php")
    browser = Wrapper(driver)
    yield browser
    conn = DbConnection("111")
    conn.delete_db()
    driver.quit()


@pytest.fixture(scope="module")
def app(browser):
    all_instances = Application(browser)
    return all_instances

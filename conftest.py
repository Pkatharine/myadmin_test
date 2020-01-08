import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from Application import Application
from wrapper import Wrapper


@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.get("http://localhost/phpmyadmin/index.php")
    browser = Wrapper(driver)
    yield browser
    driver.quit()


@pytest.fixture(scope="function")
def app(browser):
    all_instances = Application(browser)
    return all_instances

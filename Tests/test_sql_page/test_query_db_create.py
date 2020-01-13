import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



def test_query_creation_of_databases(app):
    db_name_input = (By.XPATH, '//*[@id="pma_navigation_tree_content"]/ul/li[9]/div[2]/a/img')
    new_db_name = (By.CSS_SELECTOR, '[id="new_db_name"]')
    new_db_name_submit = (By.CSS_SELECTOR, '[id="rename_db_input"]')
    db_submit_button = (By.CSS_SELECTOR, "#button_submit_query")
    time.sleep(1)
    # try:
    #     app.browser.find_element(db_name_input).text('CREATE DATABASE `test_table`')
    # except Exception == 'ElementNotInteractableError':
    #     app.driver.executeScript('(element: WebElement)')

    app.navPage.click_SQL_page()
    # time.sleep(5)
    # actions = ActionChains(app.browser)
    # actions.send_keys('CREATE DATABASE `test_table`')
    # actions.perform()
    # app.browser.
    # app.browser.find_element(db_name_input).sendKeys('CREATE DATABASE `test_table`')
    qwerty = app.browser.find_element(db_name_input)
    qwerty.click()
    app.browser.find_element(new_db_name).send_keys('qwerty')
    app.browser.find_element(new_db_name_submit).click()

    time.sleep(2000)
    app.sqlPage.click_submit()
    app.browser.driver.find_element()
    # app.sqlPage.createDBQuery('[title="SQL"]')
    # app.sqlPage.createDBQuery('CREATE DATABASE `test_table`')

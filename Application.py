from PageObjects.LeftPanel import LeftPanel
from PageObjects.SQLPage import SQLPage


class Application():

    def __init__(self, browser):
        self.browser = browser
        self.sqlPage = SQLPage(self.browser)
        self.left_panel = LeftPanel(self.browser)

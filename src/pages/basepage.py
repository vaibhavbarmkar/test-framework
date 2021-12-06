from src.common.commonactions import CommonActions

class BasePage(CommonActions):
    def __init__(self,driver):
        self.driver = driver
        super().__init__(self.driver)



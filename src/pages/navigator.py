from .basepage import BasePage
from selenium.webdriver.common.by import By
import os,logging


class Navigation(BasePage):

    def __init__(self,driver):
        self.driver = driver
        super().__init__(self.driver)

    def navigate_to(self, path):
        path = os.getenv("BASEURL") + path
        logging.info("Navigating to {}".format(path))
        self.driver.get(path)
        logging.info("Navigated to {}".format(path))

    def navigate_to_module(self, module_name):
        try:
            logging.info("Navigating to module {}".format(module_name))
            locator = "li[data-tab-item='org-header-{}-tab'] a".format(module_name)
            logging.info("Navigating to module selector is {}".format(locator))
            module_element = self.driver.find_element(By.CSS_SELECTOR, locator)
            self.wait_for_element_to_visible(module_element)
            self.click(module_element)
            logging.info("Navigated to module {}".format(module_name))
        except Exception as e:
            logging.error("Error occured while navigating to module {}".format(module_name))
            raise e("Error occured while navigating to module {}".format(module_name))



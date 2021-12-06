import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service
import logging


class Driver:

    def __init__(self):
        self.driver = None

    def load_driver(self):
        try:
            browser_name = os.getenv("BROWSER")
            logging.info("Creating session for {} browser".format(browser_name))
            if browser_name.lower() == "chrome":
                s = Service(ChromeDriverManager().install())
                self.driver = webdriver.Chrome(service=s)
            elif browser_name.lower() == "edge":
                s = Service(executable_path=EdgeChromiumDriverManager().install())
                self.driver = webdriver.Edge(service=s)
            elif browser_name.lower() == "firefox":
                s = Service(executable_path=GeckoDriverManager().install())
                self.driver = webdriver.Firefox(service=s)
            else:
                raise Exception("provided option is not  valid {}".format(browser_name))
            self.driver.maximize_window()
            return self.driver
        except Exception as e:
            logging.error("Error occured while initializing browser {}".format(browser_name))
            logging.exception(e)

    def get_driver_obj(self):
        if self.driver is None:
            self.load_driver()
        return self.driver

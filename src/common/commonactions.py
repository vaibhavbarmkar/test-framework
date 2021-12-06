import selenium.webdriver.support.wait as wait
from selenium.webdriver.support import expected_conditions as EC
import os,logging


class CommonActions:

    def __init__(self,driver):
        self.driver =driver
        self.web_driver_wait = wait.WebDriverWait(self.driver, os.getenv("WAITTIMEOUT"))

    def wait_for_element_to_visible(self, element):
        self.web_driver_wait.until(
            EC.visibility_of(element), "element is not present")

    def click(self,element):
        self.wait_for_element_to_visible(element)
        element.click()

    def get_text(self,element):
        self.wait_for_element_to_visible(element)
        return element.text

from src.pages.basepage import BasePage
from selenium.webdriver.common.by import By
import logging


class RepoPage(BasePage):

    repository_list_base = (By.CSS_SELECTOR, "#org-repositories .flex-auto")
    repository_names = (By.CSS_SELECTOR, "h3 a")
    repository_descriptions = (By.CSS_SELECTOR, "p")

    def __init__(self,driver):
        self.driver = driver
        super().__init__(self.driver)

    def get_repo_list_name_and_description(self):
        try:
            repo_list_names = self.driver.find_elements(*RepoPage.repository_list_base)
            repo_name_and_description = []
            for i in repo_list_names:
                name = i.find_element(*RepoPage.repository_names).text
                desc= "empty"
                try:
                    desc = i.find_element(*RepoPage.repository_descriptions).text
                except:
                    pass
                data = {}
                data[name] = desc
                repo_name_and_description.append(data)
            return repo_name_and_description
        except Exception as e:
            logging.error("Error occured while getting repository name and description")
            raise e





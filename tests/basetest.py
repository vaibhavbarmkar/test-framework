import pytest
from src.pages.navigator import Navigation
from src.pages.repopage import RepoPage
from src.businesslib.api.repositoriesapi import RepositoriesApi
import logging


@pytest.mark.usefixtures("driver_get")
class TestBase:

    def setup_class(self):
        logging.info("Starting setup class")
        self.navigation = Navigation(self.driver)
        self.repopage = RepoPage(self.driver)
        self.repositoriesapi = RepositoriesApi()
        logging.info("Completed setup class")

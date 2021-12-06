from tests.basetest import TestBase
from src.utils.helper_functions import HelperFunctions
import pytest


class TestGithubRep(TestBase):

    def setup_method(self):
        self.navigation.navigate_to("/django")

    @pytest.mark.smoke
    def test_repo_list_pass(self):
        self.navigation.navigate_to_module('repositories')
        actual_data = self.repopage.get_repo_list_name_and_description()
        expected_data = self.repositoriesapi.get_repo_name_and_description()
        result = HelperFunctions.compare_jsons(expected_data,actual_data)
        assert result is True

    def test_repo_list_fail(self):
        self.navigation.navigate_to_module('repositories')
        actual_data = self.repopage.get_repo_list_name_and_description()
        expected_data = self.repositoriesapi.get_repo_name_and_description()
        result = HelperFunctions.compare_jsons(expected_data,actual_data)
        assert result is False

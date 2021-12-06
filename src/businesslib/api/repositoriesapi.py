from src.common.apibase import ApiBase


class RepositoriesApi():
    """
    This class is used for working with repositories API
    """

    def __init__(self):
        pass

    def get_repo_name_and_description(self):
        """
        This function is calls the repository API and extract name and description for all repos
        :return: List Returns list of json object
        """
        response = ApiBase.get_request(ApiBase.get_endpoint("repositories"))
        repo_name_and_desc = []
        for node in response.json():
            repo_name = node["name"]
            desc = node["description"] if node["description"] is not None else "empty"
            data ={}
            data[repo_name] = desc
            repo_name_and_desc.append(data)

        return repo_name_and_desc

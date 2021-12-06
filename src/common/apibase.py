import requests,os,logging,json

class ApiBase:

    @staticmethod
    def get_endpoint(module_name):
        file = open(os.getenv("ENDPOINTPATH"))
        data = json.load(file)
        return data[module_name]


    @staticmethod
    def get_request(url,headers = None, param = None):
        """
        This function is used for GET call
        :param url: Request url without base url
        :param headers: request headers
        :param param: data required to make api call
        :return: Response response of API call
        """
        return ApiBase._make_request("GET",url,headers,param)

    @staticmethod
    def post_request(url, headers = None, param = None):
        """
        This function is used for POST call
        :param url: Request url without base url
        :param headers: request headers
        :param param: data required to make api call
        :return: Response response of API call
        """
        return ApiBase._make_request("POST",url,headers,param)

    @staticmethod
    def put_request(url, headers = None, param = None):
        """
        This function is used for PUT call
        :param url: Request url without base url
        :param headers: request headers
        :param param: data required to make api call
        :return: Response response of API call
        """
        return ApiBase._make_request("PUT",url,headers,param)

    @staticmethod
    def delete_request(url, headers = None, param = None):
        """
        This function is used for DELETE call
        :param url: Request url without base url
        :param headers: request headers
        :param param: data required to make api call
        :return: Response response of API call
        """
        return ApiBase._make_request("DELETE",url,headers,param)

    @staticmethod
    def patch_request(url, headers = None, param = None):
        """
        This function is used for PATCH call
        :param url: Request url without base url
        :param headers: request headers
        :param param: data required to make api call
        :return: Response response of API call
        """
        return ApiBase._make_request("PATCH",url,headers,param)

    @staticmethod
    def _check_response(response):
        """
        This function is used for checking API response is ok
        :param response:
        :return: Response
        """
        if not response.ok:
            raise Exception("API call is not successful")
        return response

    @staticmethod
    def _make_request(method,url,headers,param):
        """
        This function is used for making request based on provided parameters
        :param method: Method name from GET,PUT,POST,DELETE,PATCH
        :param url: Request url without base url
        :param headers: request headers
        :param param: data required to make api call
        :return: Response response of API call
        """
        url = os.getenv("APIBASEURL") + url

        if headers is None:
            headers = {}
        headers.update({'Accpet': 'application/vnd.github.v3+json'})
        if param is None:
            param = {}
        logging.info("Making {} request using url {}, header {} and param {}".format(method,url,str(headers),str(param)) )
        if method == 'GET':
            response = requests.get(url, params=param, headers=headers)
        elif method == 'POST':
            response = requests.post(url, data=param, headers=headers)
        elif method == 'PUT':
            response = requests.put(url, data=param, headers=headers)
        elif method == 'DELETE':
            response = requests.delete(url, data=param, headers=headers)
        elif method == 'PATCH':
            response = requests.patch(url, data=param, headers=headers)
        else:
            raise Exception(f'Bad HTTP method "{method}" was received')
        return ApiBase._check_response(response)

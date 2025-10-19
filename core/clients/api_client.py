from http.client import responses

import requests
import os
from dotenv import load_dotenv
from core.settings.environment import Environment

load_dotenv()

class ApiClient:
    def __init__(self):
        environment_str= os.getenv("Environment")
        try:
            environment = Environment[environment_str]
        except KeyError:
            raise ValueError (f"unsupported environment value: {environment_str}")

        self.base_url = self.get_base_url(environment)
        self.headers = {
            "Content-Type":"application/json"
        }
    def get_base_url(self, environment : Environment) -> str:
        if environment == Environment.TEST:
            return ("TEST_BASE_URL")
        elif environment == Environment.PROD:
            return ("PROD_BASE_URL")
        else:
            raise ValueError(f"unsupported environment value: {environment}")
    def get(self, endpoint, params=None,status_code=200):
        url = self.base_url + endpoint
        response = requests.get(url, headers=self.headers,params=params)
        if status_code:
            assert response.status_code=status_code
        return response.json()
    def post(self, endpoint, data=None,status_code=200):
        url = self.base_url + endpoint
        response = requests.post(url, headers=self.headers,params=data)
        if status_code:
            assert response.status_code=status_code
        return response.json()
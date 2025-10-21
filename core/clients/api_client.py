from http.client import responses

import requests
import os
from dotenv import load_dotenv
from core.settings.environment import Environment
import allure
from core.clients.endpoints import Endpoints
from core.settings.config import Users,Timeouts

load_dotenv()

class ApiClient:
    def __init__(self):
        environment_str = os.getenv("Environment")
        try:
            environment = Environment[environment_str]
        except KeyError:
            raise ValueError (f"unsupported environment value: {environment_str}")

        self.base_url = self.get_base_url(environment)
        self.session = requests.Session()
        self.session.headers = {
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
            assert response.status_code == status_code
        return response.json()

    def post(self, endpoint, data=None,status_code=200):
        url = self.base_url + endpoint
        response = requests.post(url, headers=self.headers,params=data)
        if status_code:
            assert response.status_code == status_code
        return response.json()

    def ping(self):
        with allure.step("Ping api client"):
            url = f"{self.base_url}{Endpoints.PING_ENDPOINT}"
            response = self.session.get(url)
            response.raise_for_status()
        with allure.step("Checking status code"):
            assert response.status_code == 201, f"Expected status code 201, but get {response.status_code}"
        return response.status_code

    def auth(self):
        with allure.step("Ping api client"):
            url = f"{self.base_url}{Endpoints.AUTH_ENDPOINT}"
            payload = {"username":Users.USERNAME,"password":Users.PASSWORD}
            response = self.session.post(url, json=payload,timeout=Timeouts.TIMEOUT)
            response.raise_for_status()
        with allure.step("Checking status code"):
            assert response.status_code ==200, f"Expected status code 201, but get {response.status_code}"
        token = response.json().get("token")
        with allure.step("Updating header with autorization"):
            self.session.headers.update({"Autorization": f"Bearer{token}"})

    def get_booking_by_id(self):
        with allure.step("Get booking IDs"):
            url = f"{self.base_url}{Endpoints.BOOKING_ENDPOINT}"
            response = self.session.get(url, timeout=Timeouts.TIMEOUT)
            response.raise_for_status()
        with allure.step("Checking status code"):
            assert response.status_code == 200, f"Expected status code 201, but get {response.status_code}"
        return response.json()["object"]



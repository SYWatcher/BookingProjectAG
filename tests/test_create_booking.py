import allure
import pytest
import requests
from core.clients.endpoints import Endpoints

from conftest import api_client

allure.feature("Test create booking")
allure.story("Create booking")
def test_create_booking(api_client):
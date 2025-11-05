import allure
import pytest
import requests

from core.clients.api_client import ApiClient


allure.feature("Test create booking")
allure.story("Create booking")
def test_create_booking(api_client, generate_random_booking_data):
    booking_data = generate_random_booking_data
    with allure.step("Create a new booking"):
        response = api_client.create_booking(booking_data)
    with allure.step("Return id booking"):
        assert isinstance(response["bookingid"], int)
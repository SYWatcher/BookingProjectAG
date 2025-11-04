import allure
import pytest
import requests

from core.clients.api_client import ApiClient

from conftest import api_client

allure.feature("Test create booking")
allure.story("Create booking")
def test_create_booking(api_client, generate_random_booking_data, booking_dates):
    booking_data = {
        "firstname": generate_random_booking_data["firstname"],
        "lastname": generate_random_booking_data["lastname"],
        "totalprice": generate_random_booking_data["totalprice"],
        "depositpaid": generate_random_booking_data["depositpaid"],
        "bookingdates": booking_dates,
        "additionalneeds": generate_random_booking_data["additionalneeds"]
    }
    with allure.step("Create a new booking"):
        response = api_client.create_booking(booking_data)
    with allure.step("Return id booking"):
        assert isinstance(response["bookingid"], int)
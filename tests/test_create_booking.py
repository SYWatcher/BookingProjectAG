import allure
import pytest
import requests
from pydantic import ValidationError
from models.booking import Booking, BookingResponse

from core.clients.api_client import ApiClient

@allure.feature("Test creating booking")
@allure.story("Positive: creating booking with custom data")
def test_create_booking_with_custom_data(api_client):
    booking_data = {
        "firstname": "Ivan",
        "lastname": "Ivanovich",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-02-01",
            "checkout": "2025-02-10"
        },
        "additionalneeds": "Dinner"
    }
    response = api_client.create_booking(booking_data)
    try:
        BookingResponse(**response)
    except ValidationError as e:
        raise ValidationError (f"Response validation error {e}")

    assert response ["booking"]["firstname"] == booking_data ["firstname"]
    assert response ["booking"]["lastname"] == booking_data ["lastname"]
    assert response ["booking"]["totalprice"] == booking_data["totalprice"]
    assert response ["booking"]["depositpaid"] == booking_data["depositpaid"]
    assert response ["booking"]["bookingdates"]["checkin"] == booking_data["bookingdates"]["checkin"]
    assert response ["booking"]["bookingdates"]["checkout"] == booking_data["bookingdates"]["checkout"]
    assert response ["booking"]["firstname"] == booking_data["firstname"]
    assert response ["booking"]["additionalneeds"] == booking_data["additionalneeds"]

@allure.feature("Test create booking")
@allure.story("Create booking with random data")
def test_create_booking(api_client, generate_random_booking_data):
    with allure.step("Create a new booking"):
        response = api_client.create_booking(generate_random_booking_data)
    with allure.step("Return id booking"):
        assert isinstance(response["bookingid"], int)

@allure.feature("Test create booking")
@allure.story("Negative: Create booking with wrong type fields")
def test_create_booking_wrong_type(api_client, generate_random_booking_data_with_wrong_type, mocker):
    mock_response = mocker.Mock()
    mock_response.status_code = 500
    mocker.patch.object(api_client.session, 'post', return_value=mock_response)
    with pytest.raises(AssertionError, match="Expected status code 200, but get 500"):
        api_client.create_booking(generate_random_booking_data_with_wrong_type)

@allure.feature("Test create booking")
@allure.story("Create booking with past data")
def test_create_booking_past_date(api_client, generate_random_booking_data_with_past_date):
    with allure.step("Create a new booking"):
        response = api_client.create_booking(generate_random_booking_data_with_past_date)
    with allure.step("Return id booking"):
        assert isinstance(response["bookingid"], int)
        assert response["booking"]["firstname"] == generate_random_booking_data_with_past_date["firstname"]
        assert response["booking"]["lastname"] == generate_random_booking_data_with_past_date["lastname"]
        assert response["booking"]["totalprice"] == generate_random_booking_data_with_past_date["totalprice"]
        assert response["booking"]["depositpaid"] == generate_random_booking_data_with_past_date["depositpaid"]
        assert response["booking"]["bookingdates"]["checkin"] == generate_random_booking_data_with_past_date["bookingdates"]["checkin"]
        assert response["booking"]["bookingdates"]["checkout"] == generate_random_booking_data_with_past_date["bookingdates"]["checkout"]
        assert response["booking"]["firstname"] == generate_random_booking_data_with_past_date["firstname"]
        assert response["booking"]["additionalneeds"] == generate_random_booking_data_with_past_date["additionalneeds"]

@allure.feature("Test create booking")
@allure.story("Negative: Create booking with wrong type fields")
def test_create_booking(api_client, generate_random_booking_data_with_wrong_type):
    response = api_client.create_booking(generate_random_booking_data_with_wrong_type)
    assert response["booking"]["firstname"] == generate_random_booking_data_with_wrong_type["firstname"]
    assert response["booking"]["lastname"] == generate_random_booking_data_with_wrong_type["lastname"]
    assert response["booking"]["totalprice"] == generate_random_booking_data_with_wrong_type["totalprice"]
    assert response["booking"]["depositpaid"] == generate_random_booking_data_with_wrong_type["depositpaid"]
    assert response["booking"]["bookingdates"]["checkin"] == generate_random_booking_data_with_wrong_type["bookingdates"]["checkin"]
    assert response["booking"]["bookingdates"]["checkout"] == generate_random_booking_data_with_wrong_type["bookingdates"]["checkout"]
    assert response["booking"]["firstname"] == generate_random_booking_data_with_wrong_type["firstname"]
    assert response["booking"]["additionalneeds"] == generate_random_booking_data_with_wrong_type["additionalneeds"]

@allure.feature("Test create booking")
@allure.story("Create booking with unicode symbols")
def test_create_booking(api_client, generate_random_booking_data_with_unicode):
    response = api_client.create_booking(generate_random_booking_data_with_unicode)
    assert response["booking"]["firstname"] == generate_random_booking_data_with_unicode["firstname"]
    assert response["booking"]["lastname"] == generate_random_booking_data_with_unicode["lastname"]
    assert response["booking"]["totalprice"] == generate_random_booking_data_with_unicode["totalprice"]
    assert response["booking"]["depositpaid"] == generate_random_booking_data_with_unicode["depositpaid"]
    assert response["booking"]["bookingdates"]["checkin"] == generate_random_booking_data_with_unicode["bookingdates"]["checkin"]
    assert response["booking"]["bookingdates"]["checkout"] == generate_random_booking_data_with_unicode["bookingdates"]["checkout"]
    assert response["booking"]["firstname"] == generate_random_booking_data_with_unicode["firstname"]
    assert response["booking"]["additionalneeds"] == generate_random_booking_data_with_unicode["additionalneeds"]

@allure.feature("Test create booking")
@allure.story("Negative: Create booking without firstname")
def test_create_booking_no_firstname(api_client):
    booking_data = {
        "lastname": "Ivanovich",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-02-01",
            "checkout": "2025-02-10"
        },
        "additionalneeds": "Dinner"
    }
    with pytest.raises(AssertionError, match = "Expected status code 200, but get 500"):
        response = api_client.create_booking(booking_data)

@allure.feature("Test create booking")
@allure.story("Negative: Create booking with no data in firstname")
def test_create_booking_no_data(api_client):
    booking_data = {
        "firstname": None,
        "lastname": "Ivanovich",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-02-01",
            "checkout": "2025-02-10"
        },
        "additionalneeds": "Dinner"
    }
    with pytest.raises(AssertionError, match = "Expected status code 200, but get 500"):
        response = api_client.create_booking(booking_data)
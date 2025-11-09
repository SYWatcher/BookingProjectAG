from datetime import timedelta, datetime
from string import digits
from time import strftime
from faker import Faker
from core.clients.api_client import ApiClient
import pytest

@pytest.fixture(scope="session")
def api_client():
    client = ApiClient()
    client.auth()
    return client

@pytest.fixture
def booking_dates():
    today = datetime.today()
    checkin_date = today + timedelta(days=10)
    checkout_date = checkin_date + timedelta(days=5)

    return {
        "checkin": checkin_date.strftime("%Y-%m-%d"),
        "checkout": checkout_date.strftime("%Y-%m-%d")
    }

@pytest.fixture
def generate_random_booking_data(booking_dates):
    faker = Faker()
    firstname = faker.first_name()
    lastname = faker.last_name()
    totalprice = faker.random_number(digits=3)
    depositpaid = faker.boolean()
    additionalneeds = faker.sentence()

    data = {
        "firstname": firstname,
        "lastname": lastname,
        "totalprice": totalprice,
        "depositpaid": depositpaid,
        "bookingdates": booking_dates,
        "additionalneeds": additionalneeds
    }
    return data

@pytest.fixture
def booking_dates_past_date():
        today = datetime.today()
        checkin_date = today - timedelta(days=10)
        checkout_date = checkin_date + timedelta(days=5)

        return {
            "checkin": checkin_date.strftime("%Y-%m-%d"),
            "checkout": checkout_date.strftime("%Y-%m-%d")
        }

@pytest.fixture
def booking_dates_wrong_type():
    faker = Faker()
    checkin_date = faker.random_number()
    checkout_date = faker.sentence()

    return {
        "checkin": checkin_date,
        "checkout": checkout_date
    }

@pytest.fixture
def generate_random_booking_data_with_past_date(booking_dates_past_date):
    faker = Faker()
    firstname = faker.first_name()
    lastname = faker.last_name()
    totalprice = faker.random_number(digits=3)
    depositpaid = faker.boolean()
    additionalneeds = faker.sentence()

    data = {
        "firstname": firstname,
        "lastname": lastname,
        "totalprice": totalprice,
        "depositpaid": depositpaid,
        "bookingdates": booking_dates_past_date,
        "additionalneeds": additionalneeds
    }
    return data

@pytest.fixture
def generate_random_booking_data_with_wrong_type(booking_dates_wrong_type):
    faker = Faker()
    firstname = faker.first_name()
    lastname = faker.last_name()
    totalprice = faker.random_number(digits=3)
    depositpaid = faker.boolean()
    additionalneeds = faker.sentence()

    data = {
        "firstname": firstname,
        "lastname": lastname,
        "totalprice": totalprice,
        "depositpaid": depositpaid,
        "bookingdates": booking_dates_wrong_type,
        "additionalneeds": additionalneeds
    }
    return data

@pytest.fixture
def generate_random_booking_data_with_unicode(booking_dates):
    faker = Faker()
    firstname = faker.first_name()
    lastname = faker.last_name()
    totalprice = faker.random_number(digits=3)
    depositpaid = faker.boolean()
    additionalneeds = faker.random_element(elements=["☺", "★", "♥", "☀", "☁", "❄", "♫", "☎"])

    data = {
        "firstname": firstname,
        "lastname": lastname,
        "totalprice": totalprice,
        "depositpaid": depositpaid,
        "bookingdates": booking_dates,
        "additionalneeds": additionalneeds
    }
    return data
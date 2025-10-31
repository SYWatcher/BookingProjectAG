import allure
import pytest
import requests

allure.feature("Test Ping")
allure.story("Test connection")
def test_ping(api_client):
    status_code = api_client.ping()
    assert status_code == 201, f"Expected status code 200, but get {status_code}"

allure.feature("Test Ping")
allure.story("Test server unavailability")
def test_ping_server_unavailable(api_client, mocker):
    mocker.patch.object(api_client.session, 'get', side_effect = Exception("Server unavailable"))
    with pytest.raises(Exception, match="Server unavailable"):
        api_client.ping()

allure.feature("Test ping")
allure.story("Test wrong HTTP method")
def test_ping_wrong_method(api_client, mocker):
    mock_response = mocker.Mock()
    mock_response.status_code = 405
    mocker.patch.object(api_client.session, 'get', return_value=mock_response)
    with pytest.raises(AssertionError, match="Expected status code 201, but get 405"):
        api_client.ping()

allure.feature("Test ping")
allure.story("Test server error")
def test_ping_internal_server(api_client, mocker):
    mock_response = mocker.Mock()
    mock_response.status_code = 500
    mocker.patch.object(api_client.session, 'get', return_value=mock_response)
    with pytest.raises(AssertionError, match="Expected status code 201, but get 500"):
        api_client.ping()

allure.feature("Test ping")
allure.story("Test wrong url")
def test_ping_wrong_url(api_client, mocker):
    mock_response = mocker.Mock()
    mock_response.status_code = 404
    mocker.patch.object(api_client.session, 'get', return_value=mock_response)
    with pytest.raises(AssertionError, match="Expected status code 201, but get 404"):
        api_client.ping()

allure.feature("Test ping")
allure.story("Test connection with different code")
def test_ping_success_different_code(api_client, mocker):
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mocker.patch.object(api_client.session, 'get', return_value=mock_response)
    with pytest.raises(AssertionError, match="Expected status code 201, but get 200"):
        api_client.ping()

allure.feature("Test Ping")
allure.story("Test ping timeout")
def test_ping_timeout(api_client, mocker):
    mocker.patch.object(api_client.session, 'get', side_effect = requests.Timeout)
    with pytest.raises(requests.Timeout):
        api_client.ping()
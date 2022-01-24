import requests
import pytest

expected_response_full_payload = [{'id': 1, 'name': 'Company 1', 'reg_num': 1234567891},
                                  {'id': 2, 'name': 'Company 2', 'reg_num': 1234567892},
                                  {'id': 3, 'name': 'Company 3', 'reg_num': 1234567893}]


@pytest.mark.get_req
def test_get_all_companies(host_address_get):
    """
Given GET /companies endpoint,
When no id query provided in the request,
Then we should get all the items form the db
    """
    response = requests.get(host_address_get)
    assert response.status_code == 200
    assert response.json() == expected_response_full_payload


@pytest.mark.get_req
def test_get_company_by_valid_id(host_address_get):
    """
Given GET /companies endpoint,
When client provided a valid id query in the GET companies request,
Then should get only the item with respective id
    """
    response = requests.get(host_address_get, params={"id": 1})
    assert response.status_code == 200
    assert response.json() == [expected_response_full_payload[0]]


@pytest.mark.get_req
def test_get_company_by_unknown_id(host_address_get):
    """
Given GET /companies endpoint,
When client provides invalid id query in the GET companies request,
Then 404 status code/response should be generated
    """
    response = requests.get(host_address_get, params={"id": 5})
    assert response.status_code == 404
    assert response.json() == {'error': '404 Not Found: Resource not found. The company with id 5 not found'}


@pytest.mark.xfail
class TestFailingCases:

    def test_get_company_by_invalid_id(self, host_address_get):
        """
    Given GET /companies endpoint,
    When client provides invalid id query value,
    Then 400 status code/response should be generated
        """
        response = requests.get(host_address_get, params={"id": 'hello'})
        assert response.status_code == 400

    def test_get_company_by_unknown_query_param(self, host_address_get):
        """
    Given GET /companies endpoint,
    When client provides unknown query param,
    Then 400 status code/response should be generated
        """
        response = requests.get(host_address_get, params={"country": 'MD'})
        assert response.status_code == 400

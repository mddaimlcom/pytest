import requests
import pytest

post_data = [{'id': 1, 'name': 'Company 1', 'reg_num': 1234567891},
             {'id': 2, 'name': 'Company 2', 'reg_num': 1234567892},
             {'id': 3, 'name': 'Company 3', 'reg_num': 1234567893}]


@pytest.mark.post_req
def test_post_required_keys_only(host_address_post):
    response = requests.post(host_address_post, json={'name': 'Pentalog', 'reg_num': 100})
    assert response.status_code == 200
    assert response.json() == {'id':4}

@pytest.mark.post_req
def test_post_required_keys_and_more(host_address_post):
    response = requests.post(host_address_post, json={'name': 'CodeFactory', 'reg_num': 123, 'country': 'MD'})
    assert response.status_code == 200
    assert response.json() == {'id':5}

@pytest.mark.post_req
def test_post_insufficient_keys(host_address_post):
    response = requests.post(host_address_post, json={"id": 89,'country': 'Venezuela', 'reg_num': 100})
    assert response.status_code == 400
    assert response.json() == {"error": "400 Bad Request: Your request must have following keys ('name', 'reg_num')"}


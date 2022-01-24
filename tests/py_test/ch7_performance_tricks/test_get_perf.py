import requests
import json
import pytest


data = list()
for i in range(0, 1000): data.append({'id': 1}); data.append({'id':2}); data.append({'id': 3})


@pytest.mark.parametrize('id', data)
def test_get_company_by_id(host_address_get, id):
    """Request for a company that is not in the db"""
    r = requests.get(host_address_get, params=id)
    assert r.status_code == 200
    # assert json.loads(r.content) == {}


    # assert r.status_code == 404  # assert response status code
    # assert json.loads(r.content) == {'error': '404 Not Found: Resource for company id 0 not found'} # assert body
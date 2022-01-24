import json
import requests
import pytest
from pathlib import Path


def pytest_addoption(parser):
    parser.addoption("--host", action="store", default="http://127.0.0.1:5000")


@pytest.fixture(scope='module', autouse=True)
def host_address_get(pytestconfig):
    host_address = pytestconfig.getoption("host")
    return host_address + '/companies'


@pytest.fixture(scope='module', autouse=True)
def host_address_post(pytestconfig):
    host_address = pytestconfig.getoption("host")
    return host_address + '/companies'


@pytest.fixture(scope='module', autouse=True)
def db_file_handler():
    file_path = Path(str(Path(__file__).parent) +  '/' + '../../../app/db_bkp.json')
    with open(file_path) as f:
        content = f.read()
    yield None
    with open(file_path, 'w') as f:
        f.write(content)

@pytest.fixture(scope='module', autouse=True)
def db_content():
    file_path = Path(str(Path(__file__).parent) +  '/' + '../../../app/db_bkp.json')
    with open(file_path) as f:
        content = f.read()
    yield json.loads(content)


@pytest.fixture(scope='module')
def http_request(host_address_get):
    response = requests.get(host_address_get)
    return response


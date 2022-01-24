import pytest
from pathlib import Path
from ..helpers.Formater import TermColors

# global var
current_directory_path = Path(__file__).parent


def pytest_addoption(parser):
    """
Pytest Hook redefined for the collect options test phase.
Define the cli arg --host default
    """
    parser.addoption("--host", action="store", default="http://127.0.0.1:5000")


def pytest_itemcollected(item):
    """
Pytest Hook redefined for the Collection test phase.
Set the test scenario long description based of the function __doc__ string
    """
    par = item.parent.obj
    node = item.obj
    pref = par.__doc__.strip() if par.__doc__ else par.__class__.__name__
    suf = node.__doc__ if node.__doc__ else False
    if suf:
        item._nodeid = TermColors.CYAN.value.format(item._nodeid) + suf
    else:
        pass


@pytest.fixture(scope='module', autouse=True)
def host_address_get(pytestconfig):
    """
Address format for get request
    """
    host_address = pytestconfig.getoption("host")
    return host_address + '/companies'


@pytest.fixture(scope='module', autouse=True)
def host_address_post(pytestconfig):
    """
Address format for post requests
    """
    host_address = pytestconfig.getoption("host")
    return host_address + '/companies'


#autouse flags that this fixture is automatically triggered in each module
@pytest.fixture(scope='module', autouse=True)
def db_file_handler():
    """
Rewrite the db after each test execution.
    """
    file_path = Path(str(Path(__file__).parent) + '/' + '../../../app/db.json')
    with open(file_path) as f:
        content = f.read()
    # this part of the function plays the role of setup
    yield None
    # this part of the function plays the role of teardown
    with open(file_path, 'w') as f:
        f.write(content)

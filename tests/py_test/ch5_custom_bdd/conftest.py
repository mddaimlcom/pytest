import pytest
import yaml
from pathlib import Path

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
@pytest.fixture(scope='function', autouse=True)
def db_file_handler(request):
    """
By default for each test reset the db to its default backup content after each test execution.
Introspect the markers set for the specific test object for which the fixture is called.
If the "keep_db" is present then do not reset the db, but keep is alive at the end of the test.
    """
    bkp_file_path = Path(str(Path(__file__).parent) + '/' + '../../../app/db_bkp.json')
    db_file_path = Path(str(Path(__file__).parent) + '/' + '../../../app/db.json')
    assigned_markers = [getattr(m, 'name') for m in request.node.own_markers]
    if 'keep_db' in assigned_markers: # case when the "keep_db" marker is present
        yield None
    else:
        with open(bkp_file_path) as f: # case when the "keep_db" marker is not present
            content = f.read() # set the default content of the json file
        # this part of the function plays the role of setup. Overwrite the db.json file at the beginning of each test
        yield None
        with open(db_file_path, 'w') as f:
            f.write(content)
        # this part of the function plays the role of teardown, Overwrite the db.json file at the end of each test


def pytest_collection_modifyitems(items):
    """
Overwrite the default hook of the collection phase. Introspect the test object and check if there are markers set in
prepare key. If there are then add them to the object by invoking the 'add_marker' method.
    """
    counter = 0
    for item in items:
        # check that we are altering a test named `test_xxx`
        if 'prepare' in item.fixturenames:
            prepare_data = item.own_markers[0].kwargs['argvalues'][counter][0]
            markers = prepare_data.get('markers') if prepare_data is not None else None
            if markers:
                for marker in markers:
                    item.add_marker(marker)
            counter = counter + 1


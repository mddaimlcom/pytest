import pytest
import pickle
from selenium import webdriver
from ..helpers.common import get_absolute_path
import pprint


browser_type_mapping = {'chrome': webdriver.Chrome, 'firefox': webdriver.Firefox}


def pytest_addoption(parser):
    """
Set the default values for custom cli params
    """
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--executable", action="store", default=None)


@pytest.fixture(scope='module', autouse=True)
def browser_params(pytestconfig, request):
    """
Collect the browser params to be passed to the browser instantiation fixture
    """
    parsed_conf = dict()
    browser_config = request.node.obj.browser_args
    browser_executable = pytestconfig.getoption("executable")  # get the browser webdriver binary path if given

    if browser_executable:
        _exec_path = browser_executable
        parsed_conf.setdefault('executable_path', get_absolute_path(_exec_path))
    elif 'executable_path' in browser_config:
        _exec_path = browser_config['executable_path']
        parsed_conf.setdefault('executable_path', get_absolute_path(_exec_path))
    else:
        raise ValueError('Could not identify the browser executable location')

    if 'options' in browser_config: # case when we have options defined for the browser process
        pass
    return parsed_conf


@pytest.fixture(scope='module', autouse=True)
def browser_cookies(request):
    """
Case when we have defined cookies that needs to be injected into our browser after instantiation
    """
    browser_config = request.node.obj.browser_args
    if 'cookies' in browser_config:
        cookies_path = get_absolute_path(browser_config['cookies'])
        cookies = pickle.load(open(cookies_path, "rb"))
    else:
        cookies = None
    return cookies


@pytest.fixture(scope='module')
def browser(pytestconfig, browser_params, request, browser_cookies):
    """
Instantiate the browser at the module level > inject cookies if defined > return the browser object to the test and end
the browser process when all the module tests have been executed.
    """
    global browser_type_mapping
    domain_url = request.node.obj.browser_args['domain_url']
    browser_type = pytestconfig.getoption("browser")  # get the browser type to instantiate
    browser_gen = browser_type_mapping.get(browser_type) # get the Class responsible for instantiating the browser
    assert domain_url is not None, 'You need to provide a domain url in config'
    assert browser_gen is not None, f'No such browser type declared {browser_type}, please choose one of ' \
                                    f'{browser_type_mapping.keys()}'
    br_obj = browser_gen(**browser_params)  # browser initialization
    br_obj.get(domain_url)

    if browser_cookies: # inject cookies if defined
        for cookie in browser_cookies: br_obj.add_cookie(cookie)
        br_obj.refresh()
    # print(br_obj.get_cookies())
    yield br_obj
    # pprint.pprint(br_obj.get_cookies())
    br_obj.close()
    br_obj.quit()


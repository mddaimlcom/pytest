import requests
import yaml
import pytest
import pathlib
import os

# get the current directory path
parent_directory = pathlib.Path(__file__).parent.resolve()


def get_filter_file(dir, extension):
    """
Get the file paths of the files with a specific extension.
    """
    filtered_files = list()
    for file in os.listdir(dir):
        if file.endswith(extension):
            filtered_files.append(os.path.join(dir, file))
    return filtered_files


def parse_yaml_content(files: list, extract_key: str) -> dict:
    """
Get a list of yaml files read the content and parse into a standard dict for parametrisation
    """
    test_list = list()
    for file in files:
        with open(file, 'r') as stream:
            parsed_yaml = yaml.load(stream, Loader=yaml.FullLoader)
            filtered_content = parsed_yaml.get(extract_key)
            if filtered_content: test_list.extend(filtered_content)
    _argnames = ('prepare', 'call', 'expected')
    _argvalues = [(i.get('prepare'), i['request'], i['expected']) for i in test_list]
    _ids = [i['testname'] for i in test_list]
    return dict(argnames=_argnames, argvalues=_argvalues, ids=_ids)


# pass the yaml parsing functions to the parametrize function to generate tests
@pytest.mark.parametrize(**parse_yaml_content(get_filter_file(parent_directory, 'yaml'), 'api_tests'))
def test_api(prepare, call, expected, host_address_get):
    method = call['method'].lower()
    body = call['body']
    params = call['params']
    caller = getattr(requests, method) # http request library method to use
    response = caller(host_address_get, params=params, json=body)
    exp_status_code = expected['rc']
    exp_body = expected['body']
    assert response.status_code == exp_status_code, f'Response code dod not match the expected one ' \
                                                    f'{response.status_code} <> {exp_status_code}'
    assert response.json() == exp_body, f'Response payload did not match the expected one {response.json()} <> {exp_body}'


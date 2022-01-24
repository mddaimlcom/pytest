"""Get Companies feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
    parsers,
)
import json

expected_response_full_payload = [{'id': 1, 'name': 'Company 1', 'reg_num': 1234567891},
                                  {'id': 2, 'name': 'Company 2', 'reg_num': 1234567892},
                                  {'id': 3, 'name': 'Company 3', 'reg_num': 1234567893}]

@scenario('features/get_scenario.feature', 'On a rest db')
def test_on_a_rest_db():
    """On a rest db."""
    pass


@given(parsers.parse('There are {init_records:d} records in the db'))
def there_are_3_records_in_the_db(db_content, init_records):
    """There are 3 records in the db."""
    assert len(db_content) == init_records


@when('I perform simple get request')
def i_get_all_the_records(http_request):
    """I perform simple get request"""
    assert http_request.status_code == 200


@then(parsers.parse('I get exactly {number:d} records'))
def i_get_exactly_3_records(http_request, number):
    """I get exactly 3 records."""
    assert len(http_request.json()) == number


@then(parsers.parse('the records are as follows {records}'))
def the_records_are_as_follows_(http_request, records):
    """the records are as follows """
    assert expected_response_full_payload == json.loads(records)

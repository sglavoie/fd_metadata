import json

# Third-party library imports
import pytest

# Local imports
from fd_metadata.process import process


@pytest.fixture(scope='module')
def json_data_test():
    with open('tests/fixtures/data-package-test.json') as json_file:
        content = json_file.read()
        data = json.loads(content)
    return data


EXPECTED_RESULT_PROCESSING_DATA_PACKAGE = ['Package,profile,string,The profile of this descriptor.\n',
                                           'Package,name,string,"An identifier string. Lower case characters with `.`, `_`, `-` and `/` are allowed."\n']


def test_process_returns_valid_str(json_data_test):
    '''Check that the output is as expected from the fixture.'''
    result = process(obj_type='Package', dict_=json_data_test)
    assert result == EXPECTED_RESULT_PROCESSING_DATA_PACKAGE

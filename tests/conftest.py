import json

# Third-party library imports
import pytest


@pytest.fixture(scope='module')
def json_data_test():
    with open('tests/fixtures/data-package-test.json') as json_file:
        content = json_file.read()
        data = json.loads(content)
    return data


@pytest.fixture(scope='module')
def json_data_package():
    with open('tests/fixtures/data-package.json') as json_file:
        content = json_file.read()
        data = json.loads(content)
    return data

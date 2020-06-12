# Standard library imports
import json
import uuid

# Third-party library imports
from requests.exceptions import HTTPError
import mock
import pytest

# Local imports
from fd_metadata.common import load_remote_json, write_content, quote


EXPECTED_CSV = '''field,type,description
profile,string,The profile of this descriptor.
name,string,"An identifier string. Lower case characters, with `.`, `_`, `-` and `/` are allowed."
'''


class TestRequestsRemoteJson:
    def _mock_response(
            self,
            status=200,
            json_data=None,
            raise_for_status=None):
        '''Helper function to mock requests.'''
        mock_resp = mock.Mock()
        mock_resp.raise_for_status = mock.Mock()
        if raise_for_status:
            mock_resp.raise_for_status.side_effect = raise_for_status
        mock_resp.status_code = status
        mock_resp.json = mock.Mock(
            return_value=json_data
        )
        return mock_resp

    @mock.patch('requests.get')
    def test_load_remote_json(self, mock_get, json_data_package):
        '''Check that loading the remote JSON results in a valid request.'''
        mock_resp = self._mock_response(json_data=json_data_package)
        mock_get.return_value = mock_resp

        result = load_remote_json(
            fileurl='https://specs.frictionlessdata.io/schemas/data-package.json')
        assert result == json_data_package

    @mock.patch('requests.get')
    def test_failed_load_remote_json(self, mock_get):
        '''Make sure an exception is raised with network errors.'''
        with pytest.raises(HTTPError):
            mock_resp = self._mock_response(
                status=500, raise_for_status=HTTPError("server is down"))
            mock_get.return_value = mock_resp
            load_remote_json(
                fileurl='https://specs.frictionlessdata.io/schemas/data-package.json')


@pytest.mark.parametrize(
    'given,expected',
    [
        ('a string', 'a string'),
        ('a, comma, string', '"a, comma, string"'),
        ('', ''),
        ('a', 'a'),
        (',', '","'),
    ],
)
def test_quote_function_works(given, expected):
    '''Make sure that the "quote" function correctly quotes different strings.'''
    assert quote(given) == expected


def test_output_csv_is_as_expected(json_data_test, tmpdir):
    '''Check that the output is as expected from the fixture.'''
    temp_file = tmpdir.mkdir('sub').join('out.csv')
    write_content(data=json_data_test, destination=temp_file)
    assert temp_file.read() == EXPECTED_CSV
    assert len(tmpdir.listdir()) == 1

# Third-party library imports
import requests


def load_remote_json(fileurl: str) -> dict:
    '''Get JSON from remote, return as Python dict.'''
    resp = requests.get(fileurl)
    resp.raise_for_status()  # check for HTTPError
    return resp.json()


def quote(value: str) -> str:
    '''Add "quotes" around strings with comma(s).'''
    if ',' in value:
        value = '"' + value + '"'
    return value


def write_content(data: dict, destination: str) -> None:
    '''Write JSON schema to CSV file.'''
    # Write header
    with open(destination, 'w') as out:
        out.write('field,type,description\n')

        # Add each property being found as a row
        for key, value in data.items():
            if key == "properties":
                for prop, val in value.items():
                    field = prop
                    for k, v in val.items():
                        if k == 'description':
                            description = quote(v)
                        elif k == 'type':
                            field_type = quote(v)
                    out.write(f'{field},{field_type},{description}\n')

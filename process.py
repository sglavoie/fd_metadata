import csv
import json

# Third-party library imports
import requests

urls = [
    ['Package', 'https://specs.frictionlessdata.io/schemas/data-package.json'],
    ['Resource', 'https://specs.frictionlessdata.io/schemas/data-resource.json'],
    ['Table Schema', 'https://specs.frictionlessdata.io/schemas/table-schema.json'],
]


def load(url: str) -> dict:
    '''Get JSON from remote, return as Python dict.'''
    resp = requests.get(url)
    return resp.json()


def process(obj_type: str, dict_: dict) -> dict:
    '''Process a list of dict, append'''

    def quote(value: str) -> str:
        '''Add "quotes" around strings with comma(s).'''
        if ',' in value:
            value = '"' + value + '"'
        return value

    result = []

    for key, value in dict_.items():
        if key == "properties":
            for prop, val in value.items():
                field = prop
                for k, v in val.items():
                    if k == 'description':
                        description = quote(v)
                    elif k == 'type':
                        field_type = quote(v)
                result.append(
                    f'{obj_type},{field},{field_type},{description}\n')
    return result


if __name__ == '__main__':
    fp = 'output.csv'

    # Write header
    with open(fp, 'w') as out:
        out.write('object,field,type,description\n')

    for url in urls:
        dict_ = load(url[1])
        obj_type = url[0]
        out = process(obj_type, dict_)

        # Append to existing file
        with open(fp, 'a') as out_file:
            for row in out:
                out_file.write(row)

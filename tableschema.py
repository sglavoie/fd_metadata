# Local imports
from common import load_remote_json, write_content


def main() -> None:
    '''Retrieve and write schema to local CSV.'''
    fileurl = 'https://specs.frictionlessdata.io/schemas/table-schema.json'
    json_data = load_remote_json(fileurl)
    write_content(json_data, destination='data_output/tableschema.csv')


if __name__ == '__main__':
    main()

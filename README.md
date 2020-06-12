# Requirements

* Python 3.6 and above.
* `requests`. Use one of the following commands to get it:

      pip install requests
      pip install -r requirements.txt

# Requirements for tests

* `pytest`. Use one of the following commands to get it:

      pip install pytest
      pip install -r dev-requirements.txt

# Running

Simply execute the following command from the root directory:

    python process.py

This will create a file `output.csv` in the current directory describing the field and type of properties from the JSON schemas found here:

* https://specs.frictionlessdata.io/schemas/data-package.json
* https://specs.frictionlessdata.io/schemas/data-resource.json
* https://specs.frictionlessdata.io/schemas/table-schema.json

# Running the tests

Execute `pytest` from the root directory.

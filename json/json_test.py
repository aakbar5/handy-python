""" Read/write JSON formatted data """

import os
import json

def read_test(file_path):
    """
        Read data from a file having JSON formatted data.
    """

    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            json_data = json.load(file)
            print('Value of key_1: ', json_data['key_1'])
            print('Value of key_2: ', json_data['key_2'])
            print('Value of key_3: ', json_data['key_3'])

def write_test(file_path):
    """
        Write data into a file in JSON format.
    """
    
    data = {
        "key_1": "key_1_value",
        "key_2": "key_2_value",
        "key_3" : {
        "abc" : "abc_value",
        "xyz" : "xyv_value"
        }
    }
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4, sort_keys=False)

# Execute tests
write_test("json_test.json")
read_test("json_test.json")

""" 
Read/write JSON formatted data 

- Write json data to a file
- Load json data from a file
- Search data using key
- Add a new key:value pair
- Add a new key:value where value is type of list

"""

import os
import json

def read_test(file_path):
    """
        Read data from a file having JSON formatted data.
    """

    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            json_data = json.load(file)
            return json_data
    
    return None

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

# Write a json data to a file
print("Write a json file...")
write_test("json_test.json")

# Read a jason data from a file
print("Load a json file...")
json_data = read_test("json_test.json")


print("Type of data:   ", type(json_data))
print("Value of key_1: ", json_data['key_1'])
print("Value of key_2: ", json_data['key_2'])
print("Value of key_3: ", json_data['key_3'])

# Update loaded json data
if "key_4" in json_data:
    print("key_4 is not avialable in json data")
else:
    print("key_4 is avialable in json data")

print("Push a test in json data")
json_data['key_4'] = "test_data"

if "key_4" in json_data:
    print("key_4 is not avialable in json data")

if "key_4" in json_data:
    print("key_4 is not avialable in json data")
else:
    print("key_4 is avialable in json data")

# Add a lit to json
json_data['key_5'] = [1, 2, 3, 4, 5] 

# Print whole json data
print("--[Json data]------")
print(json.dumps(json_data, indent=4))
print("-------------------")

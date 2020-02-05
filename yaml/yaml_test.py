""" Read/write YAML formatted data """
# pip install pyyaml==3.13

import os
import yaml

class YamlDumperAvoidAlias(yaml.dumper.SafeDumper):
    """ Inheirt Yaml dumper to avoid creation of aliases """
    def ignore_aliases(self, data):
        return True

def read_test(file_path):
    """
        Read data from a file having YAML formatted data.
    """

    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            yaml_data = yaml.load(file)
            print("Type of yaml data: ", type(yaml_data))
            if isinstance(yaml_data, list):
                for idx, item in enumerate(yaml_data):
                    print("  Entry # ", idx, " is of type #", type(item))
                    for k, v in item.items():
                        print("    ", k, "-->", v)

def write_test(file_path):
    """
        Write data into a file in YAML format.
    """

    py_list = []
    py_dict = {
        'key_1': 'key_1_value',
        'key_2': 'key_2_value',
    }

    py_list.append(py_dict)
    py_list.append(py_dict)

    with open(file_path, "w") as file:
        # NOTE: (1) Using yaml.dump instead of yaml.safe_dump
        # (2) Passing own Dumper to avoid creation aliases as pyyaml create alias if objects are repeated
        yaml.dump(py_list, file, indent=4, default_flow_style=False, Dumper=YamlDumperAvoidAlias)
        file.close()

# Execute tests
read_test("yaml_test_read.yaml")
read_test("yaml_test_read_extended.yaml")
write_test("yaml_test_write.yaml")
read_test("yaml_test_write.yaml")

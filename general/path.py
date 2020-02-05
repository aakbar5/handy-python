""" Path manipulation """
import os

# Extract directory, file name with and without extension
curr_file_path = os.path.abspath(__file__)
curr_file_dir = os.path.dirname(curr_file_path)
curr_file_name_ext = os.path.basename(curr_file_path)
curr_file_name, curr_file_ext =  os.path.splitext(curr_file_name_ext)
print("Current file path: ", curr_file_path)
print("Current file dir:  ", curr_file_dir)
print("Current file name: ", curr_file_name)
print("Current file ext:  ", curr_file_ext)

# Check whether path is relative or absolute
abs_path = "/path/to/dummy.file"
print("Path '{}' is absolute? '{}'".format(abs_path, os.path.isabs(abs_path)))

rel_path = "../../path/to/dummy.file"
print("Path '{}' is absolute? '{}'".format(rel_path, os.path.isabs(rel_path)))

# Clean a pth
ran_path = "/path///to/./dummy.file"
print("Input path:", ran_path)
print("Clean path:", os.path.normpath(ran_path))

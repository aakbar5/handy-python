""" Dictionary to tuple """

def convert_dict_into_tuple(py_dict):
	"""
		Convert dictionary object to tuple.
	"""

	if not isinstance(py_dict, dict):
		return

	py_tuple = tuple([x for x in py_dict.values()])
	return py_tuple

# Simple tuple
ret = ("val1", "val2", "val3")
print(type(ret), ret)

# Conversion test
d = {'x':1, 'y':2}
ret = convert_dict_into_tuple(d)

print("dict obj:", d)
print(type(ret), ret)

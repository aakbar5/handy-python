""" Dictionary to tuple by order """

def convert_dict_into_tuple_by_order(py_dict, py_order):
	"""
		Convert dictionary object to tuple by the order
		of the elements specificed in the py_order.
	"""

	if not isinstance(py_dict, dict):
		return

	if not isinstance(py_order, list):
		return

	py_tuple = tuple(py_dict[x] for x in py_order)
	return py_tuple

# Simple tuple
ret = ("val1", "val2", "val3")
print(type(ret), ret)

# Conversion test
d = {'x':1, 'y':2}
o = ['y', 'x']
ret = convert_dict_into_tuple_by_order(d, o)

print("dict obj:", d)
print("order:   ", o)
print(type(ret), ret)

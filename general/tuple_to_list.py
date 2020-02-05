""" Tuple to list """

def convert_tuple_to_list(py_tuple):
	"""
		Convert tuple to list.
	"""

	if not isinstance(py_tuple, tuple):
		return

	return list(x for x in py_tuple)

# Simple tuple
t = ("val1", "val2", "val3")
print(type(t), t)

ret = convert_tuple_to_list(t)
print(type(ret), ret)

""" List of tuple to list """

def convert_list_of_tuple_to_list(py_list):
	"""
		Convert list of tuple(s) to plain list.
	"""

	if not isinstance(py_list, list):
		return

	return list(x for tup in py_list for x in tup)

# Simple tuple
t = ("val1", "val2", "val3")
print(type(t), t)

l = [(1,), (2, 3), (4, 5, 6), (4, 5, 6, 7)]
ret = convert_list_of_tuple_to_list(l)
print(type(l), l)
print(type(ret), ret)

l = [(1,), (2,)]
ret = convert_list_of_tuple_to_list(l)
print(type(l), l)
print(type(ret), ret)

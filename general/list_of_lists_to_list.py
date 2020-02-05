""" List of lists to list """

def convert_list_of_list_to_list(py_list):
	"""
		Convert list of list(s) to plain list.
	"""

	if not isinstance(py_list, list):
		return

	return list(x for lis in py_list for x in lis)

l = [[1], [2, 3]]
ret = convert_list_of_list_to_list(l)
print(type(l), l)
print(type(ret), ret)

l = [[1,], [2, 3], [4, 5, 6], [4, 5, 6, 7]]
ret = convert_list_of_list_to_list(l)
print(type(l), l)
print(type(ret), ret)

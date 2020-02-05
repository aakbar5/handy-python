""" List difference """

def get_lists_diff(py_list1, py_list2):
	"""
		Get elements of py_list1 which are not in py_list2.
	"""
	return list(set(py_list1) - set(py_list2))

list1 = [1, 2, 3, 4]
list2 = [1]
ret = get_lists_diff(list1, list2)
print("List1:", list1)
print("List2:", list2)
print("Diff: ", ret)
print("")

list1 = [1]
list2 = [1, 2, 3, 4]
ret = get_lists_diff(list1, list2)
print("List1:", list1)
print("List2:", list2)
print("Diff: ", ret)
print("")

list1 = [1, 2, 3, 4]
list2 = [1, 2, 3, 4]
ret = get_lists_diff(list1, list2)
print("List1:", list1)
print("List2:", list2)
print("Diff: ", ret)
print("")

list1 = [1, 2, 3, 4]
list2 = [4, 2, 3, 1]
ret = get_lists_diff(list1, list2)
print("List1:", list1)
print("List2:", list2)
print("Diff: ", ret)
print("")

list1 = [1, 2, 3, 4]
list2 = [10, 11, 12, 14, 15, 16]
ret = get_lists_diff(list1, list2)
print("List1:", list1)
print("List2:", list2)
print("Diff: ", ret)
print("")

list1 = [1, 2, 3, 4]
list2 = [6, 7, 8, 9]
ret = get_lists_diff(list1, list2)
print("List1:", list1)
print("List2:", list2)
print("Diff: ", ret)
print("")

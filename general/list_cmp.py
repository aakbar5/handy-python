""" List comparison """

def compare_two_lists(reference, to_cmp):
	"""
		Compare two python lists and return True
		if reference list is having all elements of
		to_cmp list.
	"""
	return all(elem in reference for elem in to_cmp)

list1 = [1, 2, 3, 4]
list2 = [1]
ret = compare_two_lists(list1, list2)
print("List1:", list1)
print("List2:", list2)
print("list1 is having all element of list2") if ret == True else print("Lists are different")
print("")

list1 = [1]
list2 = [1, 2, 3, 4]
ret = compare_two_lists(list1, list2)
print("List1:", list1)
print("List2:", list2)
print("list1 is having all element of list2") if ret == True else print("Lists are different")
print("")

list1 = [1, 2, 3, 4]
list2 = [1, 2, 3, 4]
ret = compare_two_lists(list1, list2)
print("List1:", list1)
print("List2:", list2)
print("list1 is having all element of list2") if ret == True else print("Lists are different")
print("")

list1 = [1, 2, 3, 4]
list2 = [4, 2, 3, 1]
ret = compare_two_lists(list1, list2)
print("List1:", list1)
print("List2:", list2)
print("list1 is having all element of list2") if ret == True else print("Lists are different")
print("")

list1 = [1, 2, 3, 4]
list2 = [10, 11, 12, 14, 15, 16]
ret = compare_two_lists(list1, list2)
print("List1:", list1)
print("List2:", list2)
print("list1 is having all element of list2") if ret == True else print("Lists are different")
print("")

list1 = [1, 2, 3, 4]
list2 = [6, 7, 8, 9]
ret = compare_two_lists(list1, list2)
print("List1:", list1)
print("List2:", list2)
print("list1 is having all element of list2") if ret == True else print("Lists are different")
print("")

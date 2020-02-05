""" Python single line for loop """

# Generate a list of numbers range 0-10
number_list = [x for x in range(10)]
print("Number list: ", number_list)

# Generate a list of numbers range 0-10
even_number_list = [x for x in range(10) if x % 2 == 0]
print("Even number list: ", even_number_list)

# Multiple two lists
# It takes each element of list1 with each element
# of list2
list1 = [2, 4, 6]
list2 = [2, 4, 6]
list3 = [x * y for x in list1 for y in list2]
print(list3)

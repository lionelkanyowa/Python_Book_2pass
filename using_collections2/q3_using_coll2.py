# Q.3: Write Python code to create a new tuple from (1, 2, 3, 4, 5). The new tuple should be in reverse order
# from the original. It should also exclude the first and last members of the original.
# The result should be the tuple (4, 3, 2).


# My Answer:
numbers = (1, 2, 3, 4, 5,)

numbers_list = list(numbers)
numbers_list.remove(1)
numbers_list.remove(5)
numbers_list.reverse()
number_tuple = tuple(numbers_list)


print(number_tuple)


# Launch School Answer:

# numbers = (1, 2, 3, 4, 5,)
# numbers_list = list(numbers)
# numbers_list.reverse()
# number_tuple = tuple(numbers_list[1:4])
# print(number_tuple)

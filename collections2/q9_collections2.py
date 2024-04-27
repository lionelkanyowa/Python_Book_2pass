# Q.9:

my_list = [1, 2, 3, [4, 5, 6]]
another_list = list(my_list)

# Given the above code, answer the following questions and explain your answers:

# 1.Are the lists assigned to my_list and another_list equal?
# 2.Are the lists assigned to my_list and another_list the same object?
# 3.Are the nested lists at index 3 of my_list and another_list equal?
# 4.Are the nested lists at index 3 of my_list and another_list the same object?

# Don't write any code for this exercise.

# 1.Yes they are equal because they have the same values.
# 2.They are different objects. Since they have a nested list. List constructor creates a new object.
# 3.They are equal because they contain the same values.
# 4.They are the same object. The list constructor performs a shallow copy.
# Shallow copies don't create new nested lists. Instead, only a reference to the nested list gets copied.

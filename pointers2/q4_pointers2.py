# Q.4: Without running this code, what will it print? Why?

dict1 = {
    'a': [1, 2, 3],
    'b': (4, 5, 6),
}

dict2 = dict(dict1)
dict1['a'][1] = 42
print(dict2['a'])

# The constructor call dict(dict1) creates a new dict (dict2) with the same key/value pairs as dict1.
# In line 9 we see that dict1 is mutated so that the key of string 'a' accesses the elements in the list and replaces
# the value 2 with value 42 on index 1.

# From my understanding, since dict2 is its own key/value pair, but in this case, it would output [1, 42, 3],
# Instead of [1, 2, 3]. When we alter the list in dict1, we are also altering the list in dict2. Even though there are
# 2 different dictionaries, they are still referencing the same list. Remember, dict constructors create shallow copies.

# Q.6: Without running this code, what will it print? Why?

set1 = {42, 'Monty Python', ('a', 'b', 'c')}
set2 = set1
set1.add(range(5, 10))
print(set2)

# Don't worry about having an exact match for the output. The important part is to show something that accurately
# represents set2.

# set2 will print the following: {42, 'Monty Python', range(5, 10), ('a', 'b', 'c')}

# set1 and set2 are two variables that are stored in different locations in memory and therefore have a different
# address.

# This result demonstrates that set1 and set2 reference the same set: if we add an element to set1, we'll see that
# element when we look at set2. The opposite is true, too: if we add something to set2, we'll see it in set1.
#
# This code also demonstrates that assigning a variable to another variable doesn't create a new object. Instead,
# Python copies a reference from the original variable (set1) into the target variable (set2).
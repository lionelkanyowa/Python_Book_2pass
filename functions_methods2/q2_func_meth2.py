# Q.2 Take a look at this code snippet:

foo = 'bar'


def set_foo():
    foo = 'qux'


set_foo()
print(foo)

# What does this program print? Why?

# The program will print 'bar' on line 11, and this is because `foo` is in scope on line 11.
# The outer `foo` variable on line 3 plays no part in the function's body. The assignment on line 7
# hides the `foo` variable from line 3, and this is called variable shadowing.


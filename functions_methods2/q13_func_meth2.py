# Q.13: Without running the following code, what do you think it will do?

def foo(first, second=3, third):
    print(first)
    print(second)
    print(third)

foo(42)

# The code above will produce an error. Given that there is an argument passed in line 8 for the first
# parameter, and a default parameter for the second parameter. There is nothing given for the third parameter.


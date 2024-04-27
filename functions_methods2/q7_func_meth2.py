# Q.7: Without running the following code, what do you think it'll do?

def foo(bar, qux):
    print(bar)
    print(qux)

foo('Hello')

# The code will produce an error because in line 1, the function passes in 2 parameters as placeholders.
# This is so that 2 arguments can be passed. However, when we call the method on line 7, only one argument is
# passed instead of 2.
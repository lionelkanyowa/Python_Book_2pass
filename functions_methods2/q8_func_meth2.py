# Q.8: Without running the following code, what do you think it will do?

def foo(bar, qux):
    print(bar)
    print(qux)


foo(42, 3.141592, 2.718)

# The code above will raise a type error. Line 1 has 2 parameters as placeholders means only 2 arguments
# can be passed when calling the method. Instead, we see that 3 arguments are passed in line 8 instead of 2.



# Q.1 What happens when you run the following program? Why do we get that result?

def set_foo():
    foo = 'bar'


set_foo()
print(foo)

# When running this code, we gget a NameError. The function has a `foo` variable in the body of
# `set_foo`. The error occurs because the 'foo' variable is insode the `set_foo` function. The
# code outside the function has now way to access the variable.

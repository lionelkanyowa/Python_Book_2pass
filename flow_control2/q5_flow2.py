# Q.5: What does this code output, and why

def is_list_empty(my_list):
    if my_list:
        print('Not Empty')
    else:
        print('Empty')


is_list_empty([])

# The following would print 'Empty'. This is because '[]' is passed as an argument in line 10. Since the else statement
# is invoked when a value is falsy, this would be the case since an empty list [] is falsy.

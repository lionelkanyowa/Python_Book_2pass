# Q.3: Without running the following code, what does it print? Why?

def bar_code_scanner(serial):
    match serial:
        case '123':
            print('Product1')
        case '113':
            print('Product2')
        case '142':
            print('Product3')
        case _:
            print('Product not found!')


bar_code_scanner('113')
bar_code_scanner(142)

# This will print the following:
# 'Product2'
# 'Product not found!'

# We get an output of 'Product2' in line 16 because of line 7-8.
# Any value that is not part of the match/case statement will default to the case in line 11.
# Therefore, line 16 will output: 'Product not found!'

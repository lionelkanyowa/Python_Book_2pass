# Q.14 Identify all of the identifiers on each line of the following code.

def multiply(left, right):
    return left * right


def get_num(prompt):
    return float(input(prompt))


first_number = get_num('Enter the first number: ')
second_number = get_num('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')

# Identifiers
# multiply() -- 3, 13
# get_num()  -- 7, 11, 12
# first_number -- 11, 13 14
# second_number -- 12, 13 14
# product -- 13, 14
# right -- 3, 4,
# left -- 3, 4
# input -- 8
# float -- 8
# prompt -- 7, 8
# print -- 14

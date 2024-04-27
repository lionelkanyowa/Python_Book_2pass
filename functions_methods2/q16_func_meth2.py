# Q.15: In the code shown below, identify all of the function names and parameters present in the code.
# Include the line numbers for each item identified.

def multiply(left, right):
    return left * right


def get_num(prompt):
    return float(input(prompt))


first_number = get_num('Enter the first number: ')
second_number = get_num('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')

# Function Names:
# multiply-line 3, 14
# get_num- line 8, 12, 13
# float- line 9
# input- line 9
# print line 15

# Parameters:
# left - line 3
# right - line 3
# prompt - line 8, 9

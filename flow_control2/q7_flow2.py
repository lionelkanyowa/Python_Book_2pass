# Q.7: Write a function that takes a single integer argument and prints a message that describes whether:

# the value is between 0 and 50 (inclusive)
# the value is between 51 and 100 (inclusive)
# the value is greater than 100
# the value is less than 0

def number_range(number):
    if number < 0:
        print(f' {number} is less than 0')
    elif number <= 50:
        print(f' {number} is between 0 and 50')
    elif number <= 100:
        print(f' {number} is between 51 and 100')
    else:
        print(f' {number} is greater than 100')


number_range(34)
number_range(12)
number_range(-5)

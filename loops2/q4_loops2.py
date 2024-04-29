# Q.4: Use a while loop to print all numbers in my_list with even values, one number per line.
# Then, print the odd numbers using a ' for' loop.

my_list = [6, 3, 0, 11, 20, 4, 17]

# The while loop
counter = 0
while counter < len(my_list):
    number = my_list[counter]

    if number % 2 == 0:
        print(number)
    counter += 1

# The for loop

for numbers in my_list:
    if numbers % 2 != 0:
        print(numbers)


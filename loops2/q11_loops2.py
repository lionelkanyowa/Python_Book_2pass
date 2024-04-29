# Q.11: Print all of the even numbers in the following list of nested lists. This time, don't use any for loops.

my_list = [
    [1, 3, 6, 11],
    [4, 2, 4],
    [9, 17, 16, 0],
]

outer_counter = 0
while outer_counter < len(my_list):
    inner_counter = 0
    while inner_counter < len(my_list[outer_counter]):
        number = my_list[outer_counter][inner_counter]
        if number % 2 == 0:
            print(number)
        inner_counter += 1
    outer_counter += 1
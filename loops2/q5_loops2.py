# Q.5: Print all of the even numbers in the following list of nested lists. Don't use any while loops.

my_list = [
    [1, 3, 6, 11],
    [4, 2, 4],
    [9, 17, 16, 0],
]

for lists in my_list:
    for inner_list in lists:
        if inner_list % 2 == 0:
            print(inner_list)


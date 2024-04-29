# Q.6: Let's try another variation on the even/odd-numbers theme.

# We'll return to the simpler one-dimensional version of my_list. In this problem, you should write code that
# creates a new list with one element for each number in my_list. If the original number is an even, then the
# corresponding element in the new list should contain the string 'even'; otherwise, the element should contain 'odd'.

# pretty-printed for clarity
# [
#     'odd', 'odd', 'even', 'odd',
#     'even', 'even', 'even', 'odd',
#     'odd', 'even', 'even'
# ]

my_list = [
    1, 3, 6, 11,
    4, 2, 4, 9,
    17, 6, 0,
]
result = []
for numbers in my_list:
    if numbers % 2 == 0:
        result.append('even')
    else:
        result.append('odd')

print(result)
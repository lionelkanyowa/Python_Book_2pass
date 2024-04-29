# Q.2: Modify the age.py program you wrote in Exercise 3 of the Input/Output chapter.
# The updated code should use a for loop to display the future ages.

age = int(input('How old are you? '))
print(f'You are {age} years old.')
print()

for ages in range(10, 50, 10):
    print(f'In {ages} years you will be {age + ages} years old. ')




# Q.17: Which of the identifiers in the following program are function names? Which are method names?
# Which are built-in functions?

def say(message):
    print(f'==> {message}')


string1 = input()
string2 = input()

say(max(string1.upper(), string2.lower()))

# Method names:
# string1.upper(), string2.lower() - line 11

# Function names:
# say() - line 4,11

# Built-in Functions:
# input()-line 8,9 ,print()-line 5, max()-line 11

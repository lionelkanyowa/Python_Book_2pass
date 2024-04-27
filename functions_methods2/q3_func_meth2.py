# Q.3 Write a program that uses a multiply function to multiply two numbers and returns the result. Ask the user to
# enter the two numbers, then output the numbers and result as a simple equation.

def multiply(x, y):
    return x * y


def get_number(prompt):
    enter = input(prompt)
    return float(enter)


num1 = get_number('Please enter your first number')
num2 = get_number('Please enter your second number')
total = multiply(num1, num2)
print(f'{num1} * {num2} = {total}')

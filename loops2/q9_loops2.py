# Q.9: Write a function that computes and returns the factorial of a number by using a for or while loop. The
# factorial of a positive integer n, signified by n!, is defined as the product of all integers between 1 and n,
# inclusive:

# n!	Expansion	        Result
# 1!	1	                 1
# 2!	1 * 2	             2
# 3!	1 * 2 * 3	         6
# 4!	1 * 2 * 3 * 4	     24
# 5!	1 * 2 * 3 * 4 * 5	 120

# You may assume that the argument is always a positive integer.

def factorial(number):
    sum = 1
    for n in range(number, 0, - 1):
        sum *= n
    return sum

print(factorial(1))
print(factorial(2))
print(factorial(3))
print(factorial(4))
print(factorial(5))
print(factorial(6))
print(factorial(7))
print(factorial(8))
print(factorial(25))

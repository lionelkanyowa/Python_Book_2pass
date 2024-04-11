# Q.2 This question may be a little challenging if your math skills are rusty. Don't be afraid to take advantage of the
# hints. Try your best to solve the problem, but don't feel compelled to complete it if you become frustrated.
#
# Use the REPL and the arithmetic operators to extract the individual digits of 4936:
#
# One place is 6.
# Tens place is 3.
# Hundreds place is 9.
# Thousands place is 4.

number = 4936
ones = number % 10
print(ones)

number = number // 10
print(number)

tens = number % 10
print(tens)

number = number // 10
print(number)

hundreds = number % 10
print(hundreds)

thousands = number // 10
print(thousands)




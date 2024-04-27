# Q.2: Can you write some code to change the value 'bye' in the following tuple to 'goodbye'?

stuff = ('hello', 'world', 'bye', 'now')

# First, we need to transform the tuple into a list.

stuff = list(stuff)
stuff[2] = 'goodbye'
stuff = tuple(stuff)

print(stuff)




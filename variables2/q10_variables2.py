# Q.10 Assume that obj already has a value of 42 when the code below starts running. Which of the subsequent statements
# reassign the variable? Which statements mutate the value of the object that obj references? Which statements do
# neither? If necessary, you can read the documentation.

obj = 'ABcd'       # assignment initialization
obj.upper()        # Neither
obj = obj.lower()  # reassignment/ mutates obj
print(len(obj))    # Neither
obj = list(obj)    # reassignment to a list
obj.pop()          # mutates the list by removing the last string in the list
obj[2] = 'X'      # mutates the list by replacing 'c' with 'X'
obj.sort()        # mutates the list by sorting the elements from lowest to highest
set(obj)          # nothing is done
obj = tuple(obj) # mutates obj into a tuple

print(obj)
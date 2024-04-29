# Q.1: The following code causes an infinite loop (a loop that never stops iterating). Why?

counter = 0

while counter < 5:
    print(counter)

# Code above does not increment. That is needed so the the the while loop can reach the condition.
# Since a while loop only runs while the condition is truthy and only stops once the condition becomes falsy,
# This loop will keep running infinitely outputting value 0 if no increment is added.




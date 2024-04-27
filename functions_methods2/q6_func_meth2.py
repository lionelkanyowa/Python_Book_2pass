# Q.6 What does the following code print?

def scream(words):
    words = words + '!!!!'
    return
    print(words)

scream('Yipeee')

# This would print nothing. The reason we won't get 'Yipeee!!!!' It Is because of the return function on
# line 3 that terminates the function before anything can be printed.



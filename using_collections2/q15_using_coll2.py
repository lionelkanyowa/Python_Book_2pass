# Q.15: Without running the following code, what values will be printed by line 10?

pets = {'Cat': 'Meow',
        'Dog': 'Bark',
        'Bird': 'Tweet',
        }

keys = pets.keys()
del pets['Dog']
pets['Snake'] = 'Sssss'
print(keys)

# Output
# My answer:
#{'Cat': 'Meow, 'Bird': 'Tweet', 'Snake': 'Sssss'}

# Actual Answer:
#['Cat', 'Bird', 'Snake']

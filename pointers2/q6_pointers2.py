# Q.6: The following program is nearly identical to that of the previous exercise. However, this time, it should
# create a shallow copy of dict1. Be careful: you're not allowed to use the copy module in this exercise.`
#
# In addition, before you run this code, can you predict the output values?

dict1 = {
    'a': [{7, 1}, ['aa', 'aaa']],
    'b': ({3, 2}, ['bb', 'bbb']),
}

dict2 = dict(dict1) # You may modify the `???` part
            # of this line

print(dict1         is dict2)
print(dict1['a']    is dict2['a'])
print(dict1['a'][0] is dict2['a'][0])
print(dict1['a'][1] is dict2['a'][1])
print(dict1['b']    is dict2['b'])
print(dict1['b'][0] is dict2['b'][0])
print(dict1['b'][1] is dict2['b'][1])

# This would likely print all True except for line 14, this is because since dict2 is a duplicate shallow copy,
# It is a different object from dict1.
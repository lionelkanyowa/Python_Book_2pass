# Q.5: Which of the following values can't be used as a key in a dict object, and why?

'cat'
(3, 1, 4, 1, 5, 9, 2)
['a', 'b']           # Not Hashable
{'a': 1, 'b': 2}     # Not Hashable
range(5)
{1, 4, 9, 16, 25}    #Not Hashable
3
0.0
frozenset({1, 4, 9, 16, 25})

# The remainder values can be used as keys because they are not hashable since they are immutable data types.


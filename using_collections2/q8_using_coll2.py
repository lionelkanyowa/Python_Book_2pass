# Q.8: Explain why the code below prints different values on lines 5 and 6.

text = "It's probably pining for the fjords!"

print(text[21:35]) #.rfind('f'))     # 8
print(text.rfind('f', 21, 35))    # 29

# In line 5 we are taking a slice of a string before using it to call rfind. The method returns
# the index of the search string in that slice.

# Line 6 does a search for the rightmost f between index 21 and 35. Since the f occurs at index 29, that's what the
# method returns.
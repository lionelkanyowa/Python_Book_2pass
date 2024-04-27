# Q.11: Consider the following table:

# Name	Country
# Alice	USA
# Francois	Canada
# Inti	Peru
# Monika	Germany
# anyu	Uganda
# Yoshitaka	Japan

# You need to write some Python code to determine the country name associated with one of the listed names.
# Your code should include the data structure(s) you need and at least one test case to ensure the code works.

# For this question, we can use a dict type. With Name being the key and Country being the value.

nationals = {
    'Alice': 'USA',
    'Francois': 'Canada',
    'Inti': 'Peru',
    'Monika': 'Germany',
    'anyu': 'Uganda',
    'Yoshitaka': 'Japan',
}

print(nationals['Monika'])
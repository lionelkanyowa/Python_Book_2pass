# Q.7: Write Python code to replace all the : characters in the string below with +.

info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'

parts = info.split(':')

final = '+'.join(parts)

print(final)


# info.replace(':', '+')
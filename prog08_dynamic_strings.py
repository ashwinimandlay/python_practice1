first = 'john'
last = 'smith'

# print john [smith] is a coder

message = first + ' [' + last + '] is a coder'
print(message)
# the above approach is difficult to understand
# so we use formatting string

msg = f'{first} [{last}] is a coder'
# curly braces are holes to be filled by the variables
print(msg)

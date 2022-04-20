# comparison operator >,<,== (equal to),!= (not equal)

# program for choosing password
# must be greater than 3 character
# less than 20 character

password = input("enter password: ")

if len(password) < 4:
    print("password too short")
elif len(password) >= 20:
    print("password too long")
else:
    print("password looks good")

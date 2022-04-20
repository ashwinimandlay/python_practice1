# weight convertor

weight = input("enter your weight: ")

units = input("(L)bs or (K)g : ")

weight_in_pounds = int(weight) / 0.45
weight_in_kg = int(weight) * 0.45

if units == 'k':
    print(f'you are {weight_in_pounds} pounds')
elif units == 'l' or 'L':
    print(f'you are {weight_in_kg} kg')
else:
    print("invalid input")

# method 2
weight_again = int(input("enter your weight"))
unit = input("(L)lb or (K)g: ")

if unit.upper() == 'K':
    # unit.upper makes sure that even if user enters
    # lowercase k then it automaticaly uppercase it
    converted = weight_again // 0.45
    # // gives integer value (otherwise / gives float)
    print(f'your weight is {converted} pounds')
elif unit.upper() == 'L':
    converter = weight_again * 0.45
    print(f'your weight is {converter} kg')

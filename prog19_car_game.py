# building car game
# help will list all commands
# start - to start the command
# stop - to stop the car
# quit - to exit
# anything else - i don't understand that ...


i = 1
while i == 1:
    command = input('> ')
    if command.upper() == 'HELP':
        print('''
        start - to start the car
        stop - to stop the car
        quit - to exit''')
    elif command.upper() == 'START':
        print('The car has started')
    elif command.upper() == 'STOP':
        print('Car has stopped')
    elif command.upper() == 'QUIT':
        break
    else:
        print("I don't understand that")

# problems :
# writing dot upper repeatedly makes code DRY(don't repeat yourself)
# get rid of indentation of help statements
# if car is again started print it is already done

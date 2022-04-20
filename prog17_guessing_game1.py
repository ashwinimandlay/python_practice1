# guessing game
# guess a number 1-9
# in 3 tries

chosen_number = 9

i = 1
# use refractor ->rename (shift + f6) to replace all i

while i <= 3:
    i += 1
    guess = int(input("Guess the number: "))
    if guess == chosen_number:
        print('You Win')
        break
    elif guess != chosen_number and i == 4:
        print('You Lose')
# while loop also has else statement

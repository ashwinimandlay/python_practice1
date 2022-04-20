# guessing game
# guess a number 1-9
# in 3 tries

secret_number = 9
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input("Guess the number: "))
    guess_count += 1
    if guess == secret_number:
        print('You win')
        break
else:
    print('you lose')

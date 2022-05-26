from ast import Break
import random
player_name = input('Please Enter your name: ')
print(f'\nWelcome to the higher/lower game, {player_name}!')
x = 'y'
while x != 'n':
    lower = int(input('Enter Lower Boundary: '))
    upper = int(input('Enter Upper Boundary: '))
    while lower >= upper:
        print('The lower boundary MUST be less than the upper boundary.')
        lower = int(input('Enter Lower Boundary: '))
        upper = int(input('Enter Upper Boundary: '))
    random_num = random.randint(lower, upper)
    guess = int(input(f'Guess a number between {lower} and {upper} '))
    done = False
    while done == False:
        if guess > random_num:
            print('Too High!')
            guess = int(input('\nPlease guess again:'))
        elif guess < random_num:
            print('Too low.')
            guess = int(input('\nPlease guess again'))
        elif guess == random_num:
            print('You got it! Congratulations :)')
            done = True

    x = input('\nDo you want to play again? (y/n): ')
    while x is not 'y' or 'n':
        x = input(f"Im sorry {player_name}, I didn't quite get that. Do you want to play again? (y/n)")
   
input('Thanks for playing! Press ENTER to exit. - Zahlbot')
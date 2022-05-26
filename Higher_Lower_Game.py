'''
Zahlen
05/25/22
User guesses a number in a set range based on the program saying "too high" or "too low"
Loops back around to the top when game ends if user wants to continue playing.
'''

import random
player_name = input('Please Enter your name: ')
print(f'\nWelcome to the higher/lower game, {player_name}!')
x = 'y'
while x != 'n': #Loops to replay game.
    lower = int(input('Enter Lower Boundary: '))
    upper = int(input('Enter Upper Boundary: '))
    while lower >= upper: #loops if lower boundary is higher than upper boundary
        print('The lower boundary MUST be less than the upper boundary.')
        lower = int(input('Enter Lower Boundary: '))
        upper = int(input('Enter Upper Boundary: '))
    random_num = random.randint(lower, upper)
    guess = int(input(f'Guess a number between {lower} and {upper} '))
    done = False
    while done == False: #Loops until user guesses correctly
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
    while x != 'y' or 'n': #loops if input isn't yes/no(y/n)
        x = input(f"Im sorry {player_name}, I didn't quite get that. Do you want to play again? (y/n)")
   
input('Thanks for playing! Press ENTER to exit. - Zahlen')

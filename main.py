import random

GuessInput = int(input(f'Guess the number between 1 and: '))

numberRandom = random.randint(1,int(f'{GuessInput}'))

while GuessInput != numberRandom:

    GuessNumber = int(input(f'Guess the number between 1 and {GuessInput}: '))
    
    if GuessNumber == numberRandom:
            print('You Guessed the Number Right!')
            break
            

    elif GuessNumber > numberRandom:
            print('Your guess was too high')
            


    elif GuessNumber < numberRandom:
            print('Your guess was too low')







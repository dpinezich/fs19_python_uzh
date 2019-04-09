import random

random_number = random.randrange(1,100)

guessed = 0

counter = 1


while random_number != guessed:
    guessed = int(input('Please input your guess: '))


    if guessed == random_number:
        print('Hoooooray you just won some chocolate!')
        print('It took you: ' + str(counter) + 'tries')
    elif guessed < random_number:
        print('Sorry your number is too small!')
    else:
        print('Sorry your number is too big!')

    counter = counter + 1

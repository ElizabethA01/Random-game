#Input from user

#Generate a number lower and upper limit
from random import randint
import sys

lower = int(sys.argv[1])
upper = int(sys.argv[2])
random_number = randint(lower, upper)

#check that input is a number between lower and upper limit
while True:
    try:
        print(random_number)
        input_num = int(input(f'Guess a number between {lower} and {upper}: '))
        if lower <= input_num <= upper:
            if input_num == random_number:
                print('You\'re a genius!')
                break #exits out of while loop
            else: 
                print('Guess again!')
        else: 
            print(f'A number from {lower} - {upper}')
    except ValueError:
        print('please enter a number')
        continue #loops it back to while true till person gets it right

"""
user gets first chance
RULES :
    2-Paper > 1-Rock
    1-Rock > 3-Scissors
    3-Scissors > 2-Paper
"""

import random

while True:
    user_choice_name = ''
    # user's choice
    choice = int(input('Enter choice : \n 1 : Rock, \n 2: Paper, \n 3: Scissors \n'))
    if choice == 1:
        user_choice_name = '1 : Rock'
    elif choice == 2:
        user_choice_name = '2 : Paper'
    elif choice == 3:
        user_choice_name = '3 : Scissors'
    else:
        print('Wrong Choice! Game Ends!')
        break

    print('You chose : ' + user_choice_name)

    # define computer's choice
    computer_choice = random.randint(1, 3)
    computer_choice_name = ''
    if computer_choice == 1:
        computer_choice_name = '1 - Rock'
    elif computer_choice == 2:
        computer_choice_name = '2 - Paper'
    else:
        computer_choice_name = '3 - Scissors'

    print('Computer chose : ' + computer_choice_name)

    # competetion
    if choice == computer_choice:
        print('Its a Draw!')
    elif choice == 1:
        if computer_choice == 2:
            print('Computer Won!')
        else:
            print('You Won!')
    elif choice == 2:
        if computer_choice == 3:
            print('Computer Won!')
        else:
            print('You Won!')
    elif choice == 3:
        if computer_choice == 1:
            print('Computer Won!')
        else:
            print('You Won!')


'''
Dice roll simulator takes in a number of times to
roll the dice and prints a list of dice roll results.
'''
import random


def roll_dice(turns: int = 1) -> list[int]:
    '''Creates a list of random integers and returns it
            Parameters:
                turns(int): user input for the amount
                            of times to roll the dice
    '''
    if turns <= 0:
        raise ValueError

    rolls: list[int] = [random.randint(1, 6) for x in range(turns)]

    return rolls

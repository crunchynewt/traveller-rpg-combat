import random


def roll_2d6():
    """Roll two six-sided dice and return the sum."""
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1 + die2

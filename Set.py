# Code Written by Justin Stevens, March 5th, 2021
# Implementation of GUI sourced from https://realpython.com/pysimplegui-python/
# To-do: Real time implementation so it gets the cards from the screen
# To-do: Better GUI visualization of the grid
# To-do: Add a hint button such that it can give one card in the solution
# To-do: Visualize solution instead of showing it as an array
from typing import Iterable
from math import floor
from card import *

def check_set(cards: Iterable[Card]) -> Iterable[Iterable[Card]]:
    assert len(cards) >= 3
    answers = []
    for i, first in enumerate(cards):
        for j, second in enumerate(cards[i+1:]):
            for k, third in enumerate(cards[j+1:]):
                if Card.valid(first, second, third):
                    answers.append((first, second, third))
    return answers

answers = check_set([])
print(answers)

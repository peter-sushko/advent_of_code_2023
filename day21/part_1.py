'''
For solving advent of code puzzles day 21.

This script solves Advent of Code Day 21 puzzles using a BFS algorithm 
with complex numbers in Python.

Author: Peter Sushko
Date: January 1, 2024

Usage:
- Ensure 'data.txt' contains the puzzle input data.
- Run this script to calculate the solution.
'''

data_dict = {complex(i,j): c for j, r in enumerate(open('data.txt','r', encoding = 'utf-8'))
                     for i, c in enumerate(r.strip())}

reverse_dict = {value: key for key, value in data_dict.items()}
TARGET_VALUE = 'S'
START_COORDINATE = reverse_dict[TARGET_VALUE] # It happens to be 65 + 65j.

def take_one_step(previous_locations: list) -> list:
    """
    Calculate new locations reachable by taking one step from given previous locations.

    Args:
        previous_locations (list): A list of complex numbers representing previous locations.

    Returns:
        list: A list of complex numbers representing new valid locations after taking one step.
    """
    new_locations = []
    steps = [1, -1, 1j, -1j]
    for prev_loc in previous_locations:
        valid_steps = [prev_loc + step for step in steps if data_dict[prev_loc + step] != '#']
        new_locations.extend(valid_steps)
    return set(new_locations)

current_location = [START_COORDINATE]
for move in range(64):
    new_location = take_one_step(current_location)
    current_location = new_location
print(len(current_location))

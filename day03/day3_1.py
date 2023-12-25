"""
This module solved problem 3 part of https://adventofcode.com/
"""

import re
import numpy as np

all_symbols=set([])
with open('data.txt', 'r', encoding='utf-8') as file:
    for row in file:
        for character in row:
            all_symbols.add(character)
digit_characters = [str(i) for i in range(10)]
allowed_set = set(digit_characters)
allowed_set.add('.')
symbols = all_symbols.difference(allowed_set)
symbols.discard('\n')
symbols #see whats a symbol

#dataset has:
#140 rows
#141 columns
mask = np.zeros((141, 140)) #initalize a 2d np array of zeros
np.set_printoptions(threshold=np.inf)

def mark_neighbors_2D(row_index, col_index, current_mask):
    """
    This function applies the mask to all neighboring cells.
    It does it by changing the values all around to 1.
    If handles going out of bound via try clause.

    Parameters:
    row_number (int): row index of the cell of interest.
    col_number (int): column index of the cell of interest.
    mask (2d np.array): numpy array containing the mask.

    Returns:
    mask (2d np.array): updated mask.

    Ex:
    mark_neighbors_2D called on X makes the following mask:

    0 0 0 0 0 0     0 0 0 0 0 0
    0 0 0 0 0 0     0 1 1 1 0 0
    0 0 X 0 0 0  -> 0 1 1 1 0 0
    0 0 0 0 0 0     0 1 1 1 0 0
    0 0 0 0 0 0     0 0 0 0 0 0
    """
    for i in range(-1, 2):
        for j in range(-1, 2):
            try:
                current_mask[row_index + i, col_index + j] = 1
            except IndexError:
                pass

    return current_mask

def mask_left_and_right(row_index, col_index, current_mask):
    """
    Sets the value 1 in a given mask array at the specified row and column,
    as well as the immediate left and right columns within the same row.

    Parameters:
    row_number (int): The row index in the mask.
    col_number (int): The column index in the mask.
    mask (array-like): The mask array in which the values are to be set.

    Returns:
    array-like: The modified mask array with values set to 1 at specified locations.
    """
    try:
        current_mask[row_index, col_index - 1] = 1
    except IndexError:
        pass
    try:
        current_mask[row_index, col_index] = 1
    except IndexError:
        pass
    try:
        current_mask[row_index, col_index + 1] = 1
    except IndexError:
        pass

    return current_mask

with open('data.txt', 'r', encoding='utf-8') as file:
    for row_number, row in enumerate(file):
        for col_number,character in enumerate(row):
            if character in symbols:
                mask = mark_neighbors_2D(row_number,col_number,mask)

with open('data.txt', 'r', encoding='utf-8') as file:
    for row_number, row in enumerate(file):
        for col_number,character in enumerate(row):
            if character.isdigit() and mask[row_number,col_number]:
                mask = mask_left_and_right(row_number,col_number,mask)

#the same code is repeated because we need to run it again.
#this is because it our longest number is 3 digits, so we need 2 mask updates
#to mask the third digit if the first is near a symbol
with open('data.txt', 'r', encoding='utf-8') as file:
    for row_number, row in enumerate(file):
        for col_number,character in enumerate(row):
            if character.isdigit() and mask[row_number,col_number]:
                mask = mask_left_and_right(row_number,col_number,mask)
SOLUTION = 0
with open('data.txt', 'r', encoding='utf-8') as file:
    for row_number, row in enumerate(file):
        STRING =  ""
        for col_number,character in enumerate(row):
            if character.isdigit() and mask[row_number,col_number]:
                STRING = STRING+character
            else:
                STRING = STRING+'.'
        numbers = re.findall(r'\d+', STRING) #find all numbers

        #Convert the list of strings to a list of integers and calculate the sum
        SOLUTION += sum(int(number) for number in numbers)
SOLUTION

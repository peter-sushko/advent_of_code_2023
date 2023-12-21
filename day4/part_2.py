import numpy as np

def prizes_in_row(row):
    """This function finds how many matches were in the card
    matches are identical numbers between and after a "|" symbol
    
    Parameters:
    row (string): one row of input
    
    Returns:
    int: number of matching numbers

    Examples:
    >>> prize_in_row('Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53')
    4
    """

    winning_set_string = row[row.find(':')+1 : row.find('|')]
    our_set_string = row[row.find('|')+1 : row.find('\n')]
    winning_set = set(winning_set_string.split(' '))
    our_set = set(our_set_string.split(' '))
    winning_set.discard('')
    our_set.discard('')
    return len(our_set.intersection(winning_set))

solution_array = np.ones(198) # Constant for length of file.
with open('data.txt', 'r', encoding='utf-8') as file:
    for index,file_row in enumerate(file):
        nums = prizes_in_row(file_row)
        solution_array[index + 1 : index + nums + 1] += solution_array[index]
        # The line above increased the counter of all cards above the current card.
solution_array.sum()

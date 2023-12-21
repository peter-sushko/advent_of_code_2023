def prize_in_row(row):
    """This function finds the winnings per row.

    Parameters:
    row (string): one row of input
    
    Returns:
    int: 2*(number of matches-1)

    Examples:
    >>> prize_in_row('Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53')
    8
    """

    winning_set_string = row[row.find(':')+1 : row.find('|')]
    our_set_string = row[row.find('|')+1 : row.find('\n')]
    winning_set = set(winning_set_string.split(' '))
    our_set = set(our_set_string.split(' '))
    winning_set.discard('')
    our_set.discard('')
    nums_of_matches = len(our_set.intersection(winning_set))
    if nums_of_matches == 0:
        return 0
    return 2**(nums_of_matches-1)

SOLUTION = 0
with open('data.txt', 'r', encoding='utf-8') as file:
    for file_row in file:
        SOLUTION += prize_in_row(file_row)
print(SOLUTION)

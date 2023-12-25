'''
For solving advent of code puzzles day 1.

https://adventofcode.com/2023/
'''

def find_digits(string):
    '''Find first and last digit in string and return them two as an integer.

    Parameters:
    string (str): A string of characters and letters without spaces.

    Returns:
    answer (int): the first digit and the last digit as a 2 digit number.

    Examples:
    >>> find_digits(2733vmmpknvgr)
    23
    '''

    first_is_found = False # Flag for the first number.
    for character in string:
        if character.isdigit():
            if first_is_found is False:
                first_number = character
                last_number = character  # To handle 1 letter cases.
                first_is_found = True
            else:
                last_number = character
    answer = int(first_number)*10 + int(last_number) #*10 for decimals.
    return answer

SOLUTION = 0
with open('data.txt', 'r', encoding = 'utf-8') as file:
    for row in file:
        SOLUTION += find_digits(row)
print(SOLUTION)

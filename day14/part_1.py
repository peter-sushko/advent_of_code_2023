"""
For solving advent of code puzzles day 14.
"""

import numpy as np

def parse_file(sample_file_path, rows=100, cols=100):
    """
    Parses a text file and returns a transposed numpy array of its content.

    :param sample_file_path: Path to the file to be parsed.
    :param rows: Number of rows for the array.
    :param cols: Number of columns for the array.
    :return: Transposed numpy array of the file content.
    """
    data_array = np.empty((rows, cols), dtype=str)

    with open(sample_file_path, 'r', encoding='utf-8') as file:
        for index, line in enumerate(file):
            if index >= rows:
                break
            cleaned_line = line.strip()[:cols]
            data_array[index] = list(cleaned_line) + [''] * (cols - len(cleaned_line))

    transpose = np.transpose(data_array)

    return transpose


def tilt_left(sample_string) -> str:
    '''Tilts the platform left.
    
    Sorts each substring, separated by a '#' character, in descending order and 
    concatenates them to form a new string. The sorting is applied to each substring 
    individually.

    Parameters:
    sample_string (str): A string that may contain multiple substrings separated by 
                         '#' characters.

    Returns:
    str: A new string formed by concatenating the sorted substrings. Each substring
         is sorted in descending order, and the original positions of '#' are preserved.

    Example:
    >>> tilt_left("..O#O.O#O..O.")
    "O..#OO.#OO..."

    '''
    soln = ''
    start = 0
    while start < len(sample_string):
        end = sample_string.find('#', start)
        if end == -1: # Handling the end of the string.
            end = len(sample_string)
        substring = ''.join(sorted(sample_string[start:end+1], reverse=True))
        soln = soln + substring
        start = end + 1
    return soln

def find_score(sorted_string:str) -> int:
    '''Calculated the weight on support beam.
    
    Calculates the score by summing the weights of all 'O' characters in a string.
    The weight of each 'O' character is determined by its position in the string,
    calculated as the length of the string minus the index of the 'O'.

    Parameters:
    sorted_string (str): The string in which the score is to be calculated.

    Returns:
    int: The total score, which is the sum of the weights of all 'O' characters in 
         the string.

    Example:
    >>> find_score("..#O.##O")
    6

    '''
    score = 0
    for index, char in enumerate(sorted_string):
        if char == 'O':
            score += len(sorted_string) - index
    return score


FILE_PATH = 'data.txt'
transposed_data = parse_file(FILE_PATH)

ANSWER = 0
for row in transposed_data:
    row_string = ''.join(row)
    tilted_row = tilt_left(row_string)
    ANSWER += find_score(tilted_row)
print(ANSWER)
#109098 is correct!

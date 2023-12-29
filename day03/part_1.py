'''
For solving advent of code puzzles day 3.
'''

import numpy as np

def identify_symbols(sample_file_path :str):
    '''Finds coordinates of all symbols in the map.
    
    Parameters:
    sample_file_path (str): name and path of data.


    Returns:
    symbols (list): a list of all symbols within the file. The list 
    excludes all digit symbols, as well as '.' and '\n' characters.    
    '''
    all_symbols=set([])
    with open(sample_file_path, 'r', encoding = 'utf-8') as file:
        for sample_row in file:
            for character in sample_row:
                all_symbols.add(character)

    allowed_set = set([str(i) for i in range(10)])
    allowed_set.add('.')
    symbols = all_symbols.difference(allowed_set)
    symbols.discard('\n')
    return symbols

def find_all_symbols(data_map, sample_symbols):
    '''Finds coordinates of all symbols in the map.
    
    Parameters:
    data_map (int): A 2D numpy array of the input.
    sample_symbols (list): A list of string containing symbols of interest.

    Returns:
    symbol_locations (list): A list of tuples containing the coordinates of tuples.
    '''
    symbol_locations = []
    for sample_row in range(len(data_map)):
        for column in range(len(data_map[sample_row])):
            if data_map[sample_row][column] in sample_symbols:
                symbol_locations.append((sample_row,column))
    return symbol_locations

def parse_file(sample_file_path :str):
    '''Read the file into a 2D numpt array.
    
    Parameters:
    sample_file_path (str): name and path of data.

    Returns:
    data_map (list): A 2D numpy array where each element is a character.
    '''
    data_map = np.empty((140, 140), dtype=str)

    with open(sample_file_path, 'r', encoding='utf-8') as file:
        for index, sample_row in enumerate(file, start = 1):
            row_array = np.array(list(sample_row.strip()))
            data_map[index - 1, :len(row_array)] = row_array
    return data_map

def capture_whole_number(sample_data, sample_row:int, sample_column:int):
    '''Given a coordinate of a digit, return the entire number.
    
    Parameters:
    sample_data (list): A 2D numpy array with the data.
    sample_row (int): the row coordinate of the digit.
    sample_column (int): the column coordinate of the digit.
    

    Returns:
    entire_number (int): the entire number whose digit was passed.
    
    Example:
    
    If the data_map looks like this locally:
    .......
    .......
    ..567..
    ....*..
    .......
    
    And if the coordinates of the '6' are 42, 100.
    
    >>> capture_whole_number(data_map,42,100)
    567
    '''
    output_string = ''
    if not sample_data[sample_row][sample_column].isdigit():
        return 0
    if sample_data[sample_row][sample_column-1].isdigit():
        if sample_data[sample_row][sample_column-2].isdigit():
            output_string = output_string + sample_data[sample_row][sample_column-2]
        output_string = output_string + sample_data[sample_row][sample_column-1]
    output_string = output_string + sample_data[sample_row][sample_column]

    if sample_data[sample_row][sample_column+1].isdigit():
        output_string = output_string + sample_data[sample_row][sample_column+1]
        if sample_data[sample_row][sample_column+2].isdigit():
            output_string = output_string + sample_data[sample_row][sample_column+2]
    entire_number = int(output_string)
    return entire_number

file_path = 'data.txt'
data = parse_file(file_path)
symbs = identify_symbols('data.txt')
symbol_coordinates = find_all_symbols(data,symbs)

ANSWER = 0
for symbol in symbol_coordinates:
    product = 1
    neighboring_numbers = []
    row = symbol[0]
    column = symbol[1]
    for i in range(-1,2): # Looking at the neighboring rows.
        for j in range(-1,2): # Looking at the neighboring columns.
            if data[row+i][column+j].isdigit():
                neighbor_number = capture_whole_number(data,row+i,column+j)
                neighboring_numbers.append(neighbor_number)
    for element in set(neighboring_numbers): # Using set to remove duplicates.
        ANSWER += element
print(ANSWER)

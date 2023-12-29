'''
For solving advent of code puzzles day 3 part 2.
'''

import numpy as np

def parse_file(sample_file_path :str):
    '''Read the file into a 2D numpt array.
    
    Parameters:
    sample_file_path (str): name and path of data.

    Returns:
    data_map (list): A 2D numpy array where each element is a character.
    '''
    data_map = np.empty((140, 140), dtype=str)

    with open(sample_file_path, 'r', encoding='utf-8') as file:
        for index, row in enumerate(file, start = 1):
            row_array = np.array(list(row.strip()))
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
    return int(output_string)

def find_stars(data_map):
    '''Finds coordinates of all '*' symbols in the map.
    
    Parameters:
    data_map (int): A 2D numpy array of the input.

    Returns:
    symbol_locations (list): A list of tuples containing the coordinates of '*' symbolss.
    '''
    star_locations = []
    for row in range(len(data_map)):
        for column in range(len(data_map[row])):
            if data_map[row][column] == '*':
                star_locations.append((row,column))
    return star_locations

FILE_PATH = 'data.txt'
data = parse_file(FILE_PATH)
star_coordinates = find_stars(data)

ANSWER = 0
for star_coordinate in star_coordinates:
    NUMBER_PRODUCT = 1
    gear_ratios = []
    row = star_coordinate[0]
    column = star_coordinate[1]
    for i in range(-1,2): # Looking at the neighboring rows.
        for j in range(-1,2): # Looking at the neighboring columns.
            if data[row+i][column+j].isdigit():
                gear_ratios.append(capture_whole_number(data,row+i,column+j))
    if len(set(gear_ratios)) == 2: # Needed as part of the problem.
        for element in set(gear_ratios): # Using set to remove duplicates.
            NUMBER_PRODUCT *= element
        ANSWER += NUMBER_PRODUCT
print(ANSWER)
#87467885 is too high
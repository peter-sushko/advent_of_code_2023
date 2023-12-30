'''
For solving advent of code puzzles day 13.
'''

def list_has_reflection(grid: list, pos: int):
    '''Checks if grid has a horizontal reflection at a specific position.

    Args:
        grid (list): The input grid as a list of strings.
        pos (int): The position to check for horizontal reflection.

    Returns:
        int: Returns the position multiplied by 100 if horizontal reflection is found, otherwise 0.
    '''
    length = min(pos, len(grid) - pos)
    if grid[:pos] == grid[pos:pos+length][::-1]:
        return pos*100
    if grid[pos:] == grid[pos-length:pos][::-1]:
        return pos*100
    return 0

def horizontal_reflection(grid:list):
    '''Finds the maximum horizontal reflection position in the given grid.

    Args:
        grid (list): The input grid as a list of strings.

    Returns:
        int: The position of the maximum horizontal reflection, or 0 if none is found.
    '''

    highest_output = 0
    for pos in range(1, len(grid)):
        result = list_has_reflection(grid, pos)
        highest_output = max(highest_output, result)
    return highest_output

def string_has_reflection(string: str, pos: int) -> int:
    '''Checks if a string has a vertical reflection at a specific position.

    Args:
        string (str): The input string to check for vertical reflection.
        pos (int): The position to check for vertical reflection.

    Returns:
        int: Returns 1 if a vertical reflection is found, otherwise 0.
    '''
    length = min(pos, len(string) - pos)
    if string[:pos] == string[pos:pos+length][::-1]:
        return True
    if string[pos:] == string[pos-length:pos][::-1]:
        return True
    return False

def vertical_reflection(grid: list[str]) -> int:
    '''Checks if the pattern has a vertical reflection and returns the position.

    Args:
        grid (list[str]): The input grid as a list of strings.

    Returns:
        int: The position of the vertical reflection, or 0 if none is found.
    '''
    for location in range(1,len(grid[0])):
        reflects = True
        for grid_length in range(len(grid)):
            reflects &= string_has_reflection(grid[grid_length],location)
        if reflects is True:
            return location
    return 0

FILE_PATH = 'data.txt'

with open(FILE_PATH, 'r', encoding = 'utf-8') as file:
    all_file = file.read()
    file_contents = all_file.split('\n\n')

data_list = []

for file_content in file_contents:
    lines = file_content.split('\n')
    data_list.append(lines)

ANSWER = 0
for puzzle in range(len(data_list)):
    ANSWER += horizontal_reflection(data_list[puzzle])
    ANSWER += vertical_reflection(data_list[puzzle])
print(ANSWER)

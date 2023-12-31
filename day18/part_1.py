'''
For solving advent of code puzzles day 16.

In this solution, I created a map of the excavator's path. I later
filled this map using a recursive flash flood algorithm and found its area.
'''

import sys
import numpy as np

sys.setrecursionlimit(10**6)

FILE_PATH = 'data.txt'

DATA_MAP_WIDTH = 800
DATA_MAP_HEIGHT = 900
data_map = np.zeros((DATA_MAP_WIDTH,DATA_MAP_HEIGHT)) # Size chosen to fit the problem.

curr_y = 300 # Starting y coordinate.
curr_x = 500 # Starting x coordinate.

def make_move(direction :str, steps:str, current_y :int, current_x :int) -> (int,int):
    '''Take a step in the specified direction.

    This function takes in the current coordinates and step to make.
    It outputs the position after the step is taken.

    Inputs:
    direction (str): one of the four directions: 'L', 'R', 'U', 'D'.
    steps (str): an integer for the amount of steps in the direction.
    current_y (int): current y-coordinate.
    current_x (int): current x-coordinate.
    
    Returns:
    Tuple[int, int]: A tuple containing the updated y and x coordinates.
    '''
    direction_dict = {'L':(0,-1), 'R':(0,1), 'U':(-1,0), 'D':(1,0)}
    step_y = current_y + direction_dict[direction][0] * int(steps)
    step_x = current_x + direction_dict[direction][1] * int(steps)
    return step_y, step_x

def flood_fill(matrix, row :int, col :int):
    """
    Perform flood fill on a 2D matrix starting from a specified cell.

    This function recursively explores and modifies a 2D matrix by changing
    the value of the cells from 0 to 1, starting from the given 'row' and 'col'
    coordinates and spreading to neighboring cells that are also 0, in four
    cardinal directions (up, down, left, and right).

    Parameters:
    matrix (list of list of int): A 2D matrix where the flood fill operation
        will be performed. It should contain 0s and 1s.
    row (int): The starting row index for the flood fill operation.
    col (int): The starting column index for the flood fill operation.

    Returns:
    None: The function modifies the 'matrix' in-place by changing cell values
    from 0 to 1.

    Note:
    - The function assumes that 'matrix' is a rectangular grid (all rows have
      the same number of columns).
    - It also assumes that 'row' and 'col' are valid indices within the bounds
      of 'matrix'.
    - The function does not return anything but modifies 'matrix' in-place.
    """
    # Check if the current cell is out of bounds or not zero.
    if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]) or matrix[row][col] != 0:
        return

    matrix[row][col] = 1

    flood_fill(matrix, row - 1, col)  # Up.
    flood_fill(matrix, row + 1, col)  # Down.
    flood_fill(matrix, row, col - 1)  # Left.
    flood_fill(matrix, row, col + 1)  # Right.

# The following code makes map of the path as a 2D Numpy array.

with open(FILE_PATH, 'r', encoding = 'utf-8') as file:
    for line in file:
        commands = line.split(' ')
        new_y, new_x = make_move(commands[0],commands[1],curr_y,curr_x)
        data_map[
        min(curr_y, new_y):max(curr_y, new_y) + 1,
        min(curr_x, new_x):max(curr_x, new_x) + 1
        ] = 1
        curr_x, curr_y = new_x, new_y

# Since the map is empty we now need to fill it.

# I choose these coordinates because they are inside the shape.
FLOOD_FILL_START_Y = 299
FLOOD_FILL_START_X = 501

flood_fill(data_map, FLOOD_FILL_START_Y, FLOOD_FILL_START_X)
print(int(np.sum(data_map)))

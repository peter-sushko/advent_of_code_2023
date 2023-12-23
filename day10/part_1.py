"""
For solving advent of code 2023 problem 10 part 1.
"""

import numpy as np

def find_start():
    """Find the location of the 'S' symbol."""
    with open('data.txt', 'r', encoding='utf-8') as sample_file:
        for sample_index, sample_row in enumerate(sample_file):
            if sample_row.find('S') != -1:
                return sample_index + 1, sample_row.sample_index('S')

pipe_map = np.empty((140, 140), dtype=str) # This 2d numpy array will act as a map.

with open('data.txt', 'r', encoding='utf-8') as file:
    for index, row in enumerate(file, start = 1):
        row_array = np.array(list(row.strip()))
        pipe_map[index - 1, :len(row_array)] = row_array

def symmetrical_turn(x_coordinate, y_coordinate):
    """Make a symmetrical turn.
    
    This function simulates a symmetrical turn in a pipe system. A symmetrical turn
    reflects the direction along the line y = x. Imagine a mirror from the top-right
    corner of the square to the bottom-left corner. If you enter from the left
    (x-coordinate increases by 1, y-coordinate stays the same), upon reflection, you
    will go up (y-coordinate increases) and vice versa. Similarly, if entering from
    the right, you will go down (y-coordinate decreases).

    This type of turn corresponds to pipe segments shaped like 'L' and '7'.
    
    Parameters:
    x_coordinate (int): The current x-coordinate of the direction vector.
    y_coordinate (int): The current y-coordinate of the direction vector.

    Returns:
    Tuple[int, int]: A tuple containing the new x-coordinate and the new y-coordinate
    after the symmetrical turn.
    """
    return y_coordinate, x_coordinate

def assymmetrical_turn(x_coordinate,y_coordinate):
    """Make an asymmetrical turn.
    
    This function simulates an asymmetrical turn in a pipe system. An asymmetrical turn
    reflects the direction along the line y = -x. Imagine a mirror from the top-left
    corner of the square to the bottom-right corner. If you enter from the left
    (x-coordinate increases by 1, y-coordinate stays the same), upon reflection, you
    will go down (y-coordinate decreases) and vice versa. Similarly, if entering from
    the right, you will go up (y-coordinate increases).

    This type of turn corresponds to pipe segments shaped like 'J' and 'F'.

    Parameters:
    x_coordinate (int): The current x-coordinate of the direction vector.
    y_coordinate (int): The current y-coordinate of the direction vector.

    Returns:
    Tuple[int, int]: A tuple containing the new x-coordinate and the new y-coordinate
    after the asymmetrical turn.
    """
    return -y_coordinate, -x_coordinate

def keep_straight(x_coordinate,y_coordinate):
    """To continue walking straight."""
    return x_coordinate, y_coordinate

def find_turn(x_coord, y_coord, x_step, y_step):
    """Find what turn to make based on the pipe shape."""
    if pipe_map[y_coord][x_coord] in ['-', '|']:
        new_x, new_y = keep_straight(x_step, y_step)
        return new_x, new_y

    if pipe_map[y_coord][x_coord] in ['L', '7']:
        new_x, new_y = symmetrical_turn(x_step, y_step)
        return new_x, new_y

    if pipe_map[y_coord][x_coord] in ['J', 'F']:
        new_x, new_y = assymmetrical_turn(x_step, y_step)
        return new_x, new_y

COUNTER = 1
# Starting at the coordinate 41, 110 which is right above the 'S'.
y = 40
x = 111
# to get here we walked up from the S which means y reduced by 1 and x didnt change.
y_step = -1
x_step = 0

while pipe_map[y][x] != 'S':
    x_step, y_step = find_turn(x, y, x_step, y_step)
    x += x_step
    y += y_step

    COUNTER += 1
print(int(COUNTER/2))

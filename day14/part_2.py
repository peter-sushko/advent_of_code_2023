'''
For solving advent of code puzzle day 14 part 2.

Note: the question asks for the value after 1 billion cycles.
I saved hashed values of the board states until I have a duplicate.
Using the duplicated I found a cycle and fast-forwarded to a billion.
'''
import numpy as np

def parse_file(sample_file_path, rows=100, cols=100):
    """
    Parses a text file and returns a numpy array of its content.

    :param file_path: Path to the file to be parsed.
    :param rows: Number of rows for the array.
    :param cols: Number of columns for the array.
    
    :return: A numpy array of the file content.
    """
    data_array = np.empty((rows, cols), dtype=str)

    with open(sample_file_path, 'r', encoding='utf-8') as file:
        for index, line in enumerate(file):
            if index >= rows:
                break
            cleaned_line = line.strip()[:cols]
            data_array[index] = list(cleaned_line) + [''] * (cols - len(cleaned_line))

    return data_array

def tilt_left_2d(array_2d):
    '''
    Tilts each row of a 2D NumPy array to the left within chunks separated by '#'.
    
    In each row, 'O' and '.' characters are sorted within each chunk. A chunk is 
    defined as a segment of a row between the start, end, or '#' characters. The 
    sorting moves 'O' characters to the left as much as possible within each chunk.

    Parameters:
    array_2d (numpy.ndarray): A 2D NumPy array of characters, which can include 
                              'O', '.', and '#'.

    Returns:
    numpy.ndarray: A new 2D NumPy array where each row is sorted within chunks as 
                   described, keeping '#' characters as separators.

    Example:
    >>> arr = np.array([['.', 'O', '#', '.', 'O'], ['#', 'O', '.', '.', '#']])
    >>> tilt_left_2d(arr)
    array([['O', '.', '#', 'O', '.'],
           ['#', 'O', 'O', '.', '#']])
    '''
    sorted_array = np.empty_like(array_2d)

    for i, row in enumerate(array_2d):
        sorted_row = []
        chunk = []
        for char in row:
            if char == '#':
                # Sort the current chunk and append it with the '#'.
                sorted_row.extend(sorted(chunk, reverse=True))
                sorted_row.append('#')
                chunk = []
            else:
                chunk.append(char)
        sorted_row.extend(sorted(chunk, reverse=True))

        sorted_array[i] = sorted_row

    return sorted_array


# In[4]:


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

def make_cycle(input_data):
    '''
    Each cycle tilts the platform four times so that the rounded rocks roll
    north, then west, then south, then east. After each tilt, the rounded rocks 
    roll as far as they can before the platform tilts in the next direction. After one cycle,
    the platform will have finished rolling the rocks in those four directions in that order.
    '''
    output_data = input_data
    output_data = tilt_left_2d(output_data)

    output_data = np.rot90(output_data,k=-1) # Turn counter clockwise now.
    output_data = tilt_left_2d(output_data)

    output_data = np.rot90(output_data,k=-1)
    output_data = tilt_left_2d(output_data)

    output_data = np.rot90(output_data,k=-1)
    output_data = tilt_left_2d(output_data)

    output_data = np.rot90(output_data,k=-1)

    return output_data


file_path = 'data.txt'

data = np.rot90(parse_file(file_path))
prev_states={} # Dictionary for hashed board states.
counter = 0
ANSWER = 0
REPEATS = 10**9

while counter in range(REPEATS):
    counter += 1
    data = make_cycle(data)
    state = tuple(tuple(row) for row in data) # Save the state.
    if state in prev_states:
        cycle_length = counter - prev_states[state]
        amount = (REPEATS - counter) // cycle_length
        counter += amount * cycle_length # This gets me to almost 1B.
    prev_states[state] = counter

for row in data: # Now, calculate the score.
    ANSWER += find_score(row)
print(ANSWER)

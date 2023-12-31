'''
For solving advent of code puzzles day 16 part 2.

For this problem I decided to step away from the familiar 2D Numpy arrays
and instead employ the complex numbers native to python.
The real and imaginary part allow to keep track for the 2 dimensional directions.

I parsed the file using dictionary comprehension.

For part 2, I considered starting in all 4 directions from each edge tile.
For each pair of starting locations, I combined the coordinates of visited
tiles and found the overall maximum.
'''

# Parse the file into a dictionary:
data_dictionary = {complex(i,j): c for j, r in enumerate(open('data.txt','r', encoding = 'utf-8'))
                     for i, c in enumerate(r.strip())}

STARTING_LOCATION = -1 + 0j # Starting at the top left.
STARTING_DIRECTION = 1 + 0j # Moving right.

tiles_with_beam = [(STARTING_LOCATION,STARTING_DIRECTION)]

def count_energized_tiles(tiles_to_visit: list) -> int:
    '''
    Counts the number of unique tiles energized by a beam in a grid.

    The grid is represented as a dictionary with complex numbers as keys (representing positions)
    and characters as values (representing tile types). The function simulates the movement of a 
    beam through the grid, starting from a given position and direction. The beam's direction
    changes based on the type of tile it encounters ('|', '-', '/', '\\').
    

    Args:
        tiles_to_visit (list): A list of tuples,containing a starting position (complex number)
                               and direction (complex number) for the beam.

    Returns:
        int: The number of unique tiles the beam has passed through (energized), minus one.

    Note:
        The function assumes that the grid is represented in 'data_dictionary' and has been
        populated from a file named 'data.txt'. The file should contain a grid representation 
        with specific characters.
    '''
    visited = set()  # Tracks visited positions and directions.
    while tiles_to_visit:
        current_pos, current_dir = tiles_to_visit.pop()
        while not (current_pos, current_dir) in visited:
            visited.add((current_pos, current_dir))
            current_pos += current_dir
            match data_dictionary.get(current_pos): # Check tile type and change direction.
                case '|':
                    if current_dir.imag == 0:
                        current_dir = 0 - 1j
                        tiles_to_visit.append((current_pos, -current_dir))
                case '-':
                    if current_dir.real == 0:
                        current_dir = 1 + 0j
                        tiles_to_visit.append((current_pos, -current_dir))
                case '/':
                    # Reflect the beam direction diagonally like a mirror.
                    current_dir = -1j / current_dir # Excellent time for complex algebra.
                case '\\':
                    # Reflect using the opposite diagonal.
                    current_dir = 1j / current_dir
                case None:
                    break
                # The '.' tile is ignored as it doesn't affect the direction.

    # Return the count of unique positions, starting tile doesn't count.
    return len(set(positions for positions, _ in visited)) - 1

# Find edge coordinates:
min_x = min(pos.real for pos in data_dictionary)
max_x = max(pos.real for pos in data_dictionary)
min_y = min(pos.imag for pos in data_dictionary)
max_y = max(pos.imag for pos in data_dictionary)

# Find all edge tiles:
edge_positions = [pos for pos in data_dictionary
                  if pos.real in {min_x, max_x} or pos.imag in {min_y, max_y}]

energized_tiles_counts = [] # New list to track visited tiles.

directions = [1, 1j, -1, -1j]

for pos in edge_positions:
    for direction in directions: # Trying all is simpler.
        count = count_energized_tiles([(pos - direction, direction)])
        energized_tiles_counts.append(count)
max_energized_tiles = max(energized_tiles_counts)
print(max_energized_tiles)

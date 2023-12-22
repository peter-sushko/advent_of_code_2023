"""
For solving advent of code 2023 day 5 puzzle
"""

def find_seeds():
    """This function finds all the starting seeds.
    
    The output is a list of ints.
    """
    with open('data.txt', 'r', encoding='utf-8') as file:
        first_line = file.readline()
        seeds = first_line[:-1].split(' ')
        seeds = [int(seed) for seed in seeds[1:]]  # Convert ints and skip the first element.
    return seeds


def find_indices_of_empty_rows():
    """Return the list of all blank rows"""
    indices = []
    with open('data.txt', 'r', encoding = 'utf-8') as file:
        for line_number, line in enumerate(file, start=1):
            if not line.strip():  # Check if the line is empty.
                indices.append(line_number-1)
    return indices


def find_mapping(start_index: int, end_index: int, seed_id: int):
    """ Given the start and rows of the mapping, return the mapped value.
    
    This function searches over the given segment of mapping and returns the mapped value.
    """
    for index,line in enumerate(open('data.txt', 'r', encoding='utf-8')):
        if index <= start_index + 1:
            pass
        elif index >= end_index: # If mapping not found return itself.
            return seed_id
        elif (int(line.split()[1])<=seed_id) and (int(line.split()[1])+int(line.split()[2])>=seed_id):
            return int(line.split()[0]) - int(line.split()[1]) + seed_id



SEEDS = find_seeds()
INDICES = find_indices_of_empty_rows()
ANSWER = float('inf')
for SEED in SEEDS:
    new_value = SEED
    for i in range(len(INDICES)-1):
        new_value = find_mapping(INDICES[i],INDICES[i+1],new_value)
    ANSWER =  min(ANSWER, new_value)
print(ANSWER)

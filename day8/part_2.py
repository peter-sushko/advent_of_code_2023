"""
For solving advent of code 2023 problem 8 part 2.
"""

import math

data_dict = {}
starts = []
with open('data.txt', 'r', encoding='utf-8') as file:
    path = file.readline()
    blank = file.readline() # Dealing with line 2.
    for line in file:
        key, value = line.strip().split('=')
        key = key.strip()
        if key[-1] == 'A':
            starts.append(key)
        value = value.strip()
        value = value.replace(' ','')
        value = tuple(value[1:-1].split(','))
        data_dict[key] = value
path = path[:-1]

def steps_to_solve(start: str):
    """This function finds number of steps until we arrive at a node ending in Z."""

    count = 0
    new_key = start
    while new_key[-1] != 'Z':
        new_key = data_dict[new_key][0] if path[count % len(path)] == 'L' else data_dict[new_key][1]
        count += 1
    return count


solutions = []
for start_node in starts:
    solutions.append(steps_to_solve(start_node))
print(math.lcm(*solutions))

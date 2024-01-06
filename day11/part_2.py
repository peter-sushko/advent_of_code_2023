"""
For solving advent of code 2023 problem 11.

The solution relies on the fact that the distance used in Manhattan distance.
I am using the fact that the x and y distances are independent, and I 
calculate them separately.

I store the x coordinate of each point in a list and then calculate pairwise difference.
Same is applied to the y coordinate.

I handle the "empty lines" rule by increasing the coordinate values
after each empty line.
"""

def pairwise_diffs(int_list):
    """Find the sum of all pairwise differences in a list."""
    total_sum = 0
    for i in range(len(int_list)):
        total_sum += sum(abs(int_list[i] - int_list[j]) for j in range(i + 1, len(int_list)))
    return total_sum

def increment_greater_than_key_2(lst, key):
    """This function adds 1 to all list elements greater than key."""
    return [x + 999999 if x > key else x for x in lst]

x_coords = []
y_coords = []

with open('data.txt', 'r', encoding='utf-8') as file:
    for line_number, line in enumerate(file, start=1):
        for char_number, char in enumerate(line, start=1):
            if char == '#':
                x_coords.append(char_number)
                y_coords.append(line_number)

missing_x = [value for value in range(1, 140) if value not in x_coords]
missing_y = [value for value in range(1, 140) if value not in y_coords]
for value in sorted(missing_x,reverse=True):
    x_coords = increment_greater_than_key_2(x_coords, value)
for value in sorted(missing_y,reverse=True):
    y_coords = increment_greater_than_key_2(y_coords, value)

print(pairwise_diffs(x_coords)+pairwise_diffs(y_coords))

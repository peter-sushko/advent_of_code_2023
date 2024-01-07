'''
For solving advent of code puzzles day 24 part 1.

I decided not to rely on external libraries like numpy or scipy
and write the solution using basic python functionality.

Focus for this solution was modularity, hence the
individual functions.
'''

import re

def find_intersection(line1, line2):
    """Find intersection of two lines.
    
    Calculate the intersection point of two lines 
    represented by y = m1 * x + c1 and y = m2 * x + c2.

    Args:
    line1 (tuple): (slope, intersect) of the first line.
    line2 (tuple): (slope, intersect) of the second line.

    Returns:
    tuple: (x, y) coordinates of the intersection point, or None if parallel.
    """
    m1, c1 = line1
    m2, c2 = line2

    if m1 == m2:
        return None
    x = (c2 - c1) / (m1 - m2)
    y = m1 * x + c1

    return (x, y)

def line_equation_from_points(points):
    """Find y = mx + c form.

    Compute the equation of a line in the form y = mx + c, given
    two points on the line.

    Args:
    points (tuple): (x1, y1, x2, y2) representing two points on the line.

    Returns:
    tuple: (m, c) where m is the slope and c is the y-intercept.
    Returns None if the line is vertical (infinite slope).
    """
    x1, y1, x2, y2 = points

    if x2 == x1:
        return None

    m = (y2 - y1) / (x2 - x1)  # Slope.
    c = y1 - m * x1  # Intercept.

    return (m, c)


def intersection_within_range(x, y):
    """Checks if the intersept is within the allowed range.

    Args:
    x (float): The x-coordinate of the point.
    y (float): The y-coordinate of the point.

    Returns:
    bool: True if the point is within the range, False otherwise.
    """
    min_bound = 2 * 10 ** 14
    max_bound = 4 * 10 ** 14

    return min_bound < x < max_bound and min_bound < y < max_bound

def parse_file(filename):
    """Parse the file.
    
    Parse the inpud text file to extract line segment data.

    Args:
    filename (str): The path to the file to be parsed.

    Returns:
    lines (list of tuples): Each tuple represents two points (x1, y1, x2, y2).
    """
    lines = []
    with open(filename, 'r', encoding='utf-8') as file:
        for sample_line in file:
            before_at, after_at = sample_line.split('@')
            before_numbers = [int(num) for num in re.findall(r'-?\d+', before_at)][:2]
            after_numbers = [int(num) for num in re.findall(r'-?\d+', after_at)][:2]

            second_x = before_numbers[0] + after_numbers[0]
            second_y = before_numbers[1] + after_numbers[1]
            lines.append((before_numbers[0], before_numbers[1], second_x, second_y))

    return lines

lines_standard = []

lines = parse_file('data.txt')

for line in lines:
    lines_standard.append(line_equation_from_points(line))

ANSWER = 0

for i in range(len(lines_standard) - 1):
    for j in range(i + 1, len(lines_standard)):
        intersection = find_intersection(lines_standard[i], lines_standard[j])
        if intersection is not None:
            if (lines[i][2] - lines[i][0]) / (intersection[0] - lines[i][0]) > 0:
                if (lines[j][2] - lines[j][0]) / (intersection[0] - lines[j][0]) > 0:
                    ANSWER += intersection_within_range(intersection[0], intersection[1])

print(ANSWER) #12740

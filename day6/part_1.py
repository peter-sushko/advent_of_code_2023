"""
For solving problem 6 of advent of code 2023
"""

import math
import numpy as np


def find_times_dists():
    """This function returns times and distances as two lists of ints."""
    with open('data.txt', 'r', encoding='utf-8') as file:
        first_line = file.readline()
        times_list = [int(time) for time in first_line.split() if time.isdigit()]
        second_line = file.readline()
        distances_list = [int(dist) for dist in second_line.split() if dist.isdigit()]
        return times_list, distances_list

def how_many_ways_to_win(ex_time, ex_distance):
    """ This function calculates how many way the race can be won.
    
    It finds the solution by solving a system of equations:
    x + y = time
    x * y = distance

    This system is equivalent to a quadratic:

    x**2 - x * time  + distance = 0

    np.roots find the solutions and outputs the two values.
    The number of ways to win the race is equal to the number of
    integers that are between the two solutions. 

    Example:
    >>>how_many_ways_to_win(7,9)
    4
    
    This is because the solutions to x**2 - 7*x + 9 = 0
    are 5.303 and 1.697. There are 4 total integers in this range:
    2, 3, 4 and 5. Thus we can hold the button for this amount of time
    and we will beat the distance.
    """
    sol1, sol2 = np.roots([1,-ex_time,ex_distance])
    upper_bound = math.floor(max(sol1,sol2))
    lower_bound = math.ceil(min(sol1,sol2))
    return upper_bound - lower_bound + 1

ANSWER = 1
TIMES, DISTANCES = find_times_dists()
for race in range(len(TIMES)):
    ANSWER *= how_many_ways_to_win(TIMES[race],DISTANCES[race])
print(ANSWER)

'''
For solving problem 6 part of advent of code 2023.
'''
import math
import numpy as np

def find_times_dists_part2():
    '''This function returns times and distances as ints.'''
    with open('data.txt', 'r', encoding='utf-8') as file:
        concatenated_times = ''.join(filter(str.isdigit, file.readline()))
        concatenated_dists = ''.join(filter(str.isdigit, file.readline()))
        return int(concatenated_times), int(concatenated_dists)

def how_many_ways_to_win(ex_time, ex_distance):
    '''This function calculates how many way the race can be won.
    
    It finds the solution by solving a system of equations:
    x + y = time
    x * y = distance

    This system is equivalent to a quadratic:

    x**2 - x * time  + distance = 0

    np.roots find the solutions and outputs the two values.
    The number of ways to win the race is equal to the number of
    integers that are between the two solutions. 

    Example:
    >>> how_many_ways_to_win(7,9)
    4
    
    This is because the solutions to x**2 - 7*x + 9 = 0
    are 5.303 and 1.697. There are 4 total integers in this range:
    2, 3, 4 and 5. Thus we can hold the button for this amount of time
    and we will beat the distance.
    '''
    sol1, sol2 = np.roots([1,-ex_time,ex_distance])
    upper_bound = math.floor(max(sol1,sol2))
    lower_bound = math.ceil(min(sol1,sol2))
    return upper_bound - lower_bound + 1

TIME, DISTANCE = find_times_dists_part2()
ANSWER = how_many_ways_to_win(TIME, DISTANCE)
print(ANSWER)

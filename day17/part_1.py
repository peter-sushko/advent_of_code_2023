'''
For solving advent of code puzzles day 17 part 1.

This time I once again used a dictionary of complex numbers to represent a grid.
I use a modified version of Dijkstra's algorithm to arrive at the solution.
'''

from heapq import heappop, heappush as push

data_dict = {i + j*1j: int(c) for i,r in enumerate(open('data.txt','r',encoding='utf-8'))
                    for j,c in enumerate(r.strip())}

destination = [*data_dict][-1]

def solve_maze(cnt=0):
    '''Solve the maze using a variation of Dijkstra's algorithm.

    The function uses a priority queue (min-heap) to efficiently get 
    the next position to process and a set to keep track of visited 
    positions with their directions to avoid revisiting.
    
    The maze is represented as a dictionary `data_dict`, 
    where each key is a complex number denoting a grid position (x + y*1j), 
    and the value is an integer cost to enter that grid cell.
    
    The function finds the path from the top-left corner (0,0) 
    to the bottom-right corner with the minimum total cost. It considers 
    moves in four directions.

    Parameters:
    cnt (int): A counter to track the number of nodes processed. Default is 0.

    Returns:
    int: The minimum total cost (heatloss) to reach the destination from the start position.

    '''
    nodes_to_check = [(0, 0, 0, 1), (0, 0, 0, 1j)] # First moves are left and down.
    visited_nodes = set([])

    while nodes_to_check:
        heatloss, _, position, direction = heappop(nodes_to_check)
        if position == destination: # Terminating condition.
            return heatloss
        if (position, direction) in visited_nodes:
            continue
        visited_nodes.add((position, direction))

        # Now, time for a trick: iterate over possible step sizes.
        # This means every new move is a turn.
        for step in 1j/direction, -1j/direction: # Always good time for complex algebra.
            for step_length in range(1,4): # Constant from puzzle input.
                new_position = position + step * step_length
                if new_position in data_dict: # Avoiding out of bounds errors:
                    step_loss = sum(data_dict[position+step*j] for j in range(1, step_length+1))
                    tuple_to_push = (heatloss + step_loss, cnt := cnt+  1, new_position, step)
                    push(nodes_to_check, tuple_to_push)

print(solve_maze())

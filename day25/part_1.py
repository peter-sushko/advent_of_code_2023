"""
For solving advent of code puzzles day 25 part 1.

Main Idea: Split a graph into two subsets, A and B. Initially, all nodes are in subset A. 
Remove nodes from A and keep count of how many edges lead to B.
Stop when the number is exactly three.
"""

import collections

def parse_file(filename):
    '''Parse the file.
    
    Fill the edges of the graph.
    '''
    with open(filename,'r', encoding='utf-8') as file:
        for line in file:
            main_vertex, *vertices = line.replace(':','').split()
            for vertex in vertices:
                Graph[main_vertex].add(vertex)
                Graph[vertex].add(main_vertex) # edges are bi-directional.

def count_edges(node: str, graph, subset) -> int:
    """Count the number of edges from a node to nodes outside the subset."""
    return len(graph[node] - subset)


Graph = collections.defaultdict(set)
parse_file('data.txt')
subset = set(Graph)

while sum(count_edges(node, Graph, subset) for node in subset) != 3:
    subset.remove(max(subset, key=lambda node: count_edges(node, Graph, subset)))

print(len(subset) * len(set(Graph) - subset)) #548960

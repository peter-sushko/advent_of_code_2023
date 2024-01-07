'''
For solving advent of code puzzles day 15.

'''

def hash_string(string: str):
    '''To hash like explained in the puzzle.'''
    current_value = 0
    for char in string:
        current_value += ord(char)
        current_value *= 17
        current_value = current_value % 256
    return current_value

with open('data.txt', 'r', encoding='utf-8') as file:
    first_line = file.readline()

ANSWER = 0
for substring in first_line.split(','):
    ANSWER += hash_string(substring)
print(ANSWER) #514394

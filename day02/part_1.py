'''
For solving advent of code puzzles day 2.
'''

def game_is_valid(my_string):
    '''This function return game ID if the game is valid, 0 otherwise.

    It starts finding the game ID by looking between find space and first ":" character.
    Then it loops over the code and finds the indeces of keywords "green", "blue", and "red".
    When the keyword is struck, it finds the correspoding number.
    The maximum is kept for each color.
    If all colors are less than the given count, the game is valid.
    
    Parameters:
    my_string (str): string of text passed to the function.
    Example: Game 1: 20 green, 3 red, 2 blue; 9 red, 16 blue

    Returns:
    game_number (int): ID of the game if it is valid and 0 othersize

    Examples:
    >>> ex1 = "Game 1: 20 green, 3 red, 2 blue; 9 red, 16 blue"
    >>> game_is_valid(ex1)
    0 
    because the game is invalid
    
    >>> ex2 = "Game 42: 2 green, 3 red, 2 blue; 9 red, 1 blue"
    >>> game_is_valid(ex2)
    42 
    because game ID is 42        
    '''

    game_number = int(my_string[my_string.find(" "):my_string.find(":")])
    greens = blues = reds = 0
    start_index = 0
    while start_index < len(my_string):
        found_index_green = my_string.find("green", start_index)
        if found_index_green == -1:
            pass
        else:
            greens = max(greens, int(my_string[found_index_green-3:found_index_green]))

        found_index_blue = my_string.find("blue", start_index)
        if found_index_blue == -1:
            pass
        else:
            blues = max(blues, int(my_string[found_index_blue-3:found_index_blue]))

        found_index_red = my_string.find("red", start_index)
        if found_index_red == -1:
            pass
        else:
            reds = max(reds, int(my_string[found_index_red-3:found_index_red]))
        start_index+=1

    if (reds <= 12 and greens <= 13 and blues <= 14):
        return game_number
    return 0


SOLUTION = 0
with open('data.txt', 'r', encoding = 'utf-8') as file:
    for row in file:
        SOLUTION += game_is_valid(row)
print(SOLUTION)

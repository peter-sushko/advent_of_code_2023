#!/usr/bin/env python
# coding: utf-8

# In[9]:


def game_is_valid_part2(my_string):
    """
    This function returns the product of color counts.
    Function it loops over the code and finds the indeces of keywords 
    Keywords are "green", "blue", and "red"
    When the keyword is struck, it finds the correspoding number
    The maximum is kept for each color. 
    
    Parameters:
    my_string (str): string of text passed to the function.
    Example: Game 1: 20 green, 3 red, 2 blue; 9 red, 16 blue

    Returns:
    game_number (int): the product of minimum set of cubes to make the game work

    Examples:
    >>> ex1="Game 1: 20 green, 3 red, 2 blue; 9 red, 16 blue"
    >>> game_is_valid_part2(ex1)
    >>> 2880
    because min possible green is 20, blue is 16 and red is 9. Product is 2880
    
    """
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

    return reds*greens*blues


# In[10]:


SOLUTION = 0
with open('data.txt', 'r') as file:
    for row in file:
        SOLUTION += game_is_valid_part2(row)
    print(row)
print(SOLUTION)


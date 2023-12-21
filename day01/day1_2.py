#!/usr/bin/env python
# coding: utf-8

# In[97]:


def find_digits_part2(string):
    """
    Find first and last digit in string and return them two as an integer.
    This time 'one' is a valid digit and needs to be handled.
    
    This code works

    Parameters:
    string (str): A string of characters and letters without spaces

    Returns:
    answer (int): the first digit and the last digit as a 2 digit number 

    Examples:
    >>> find_digits_part2(2733vmmpknvgr)=23
    >>> find_digits_part2(onetwothree4)=14

    """
    word_list = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    first_number = last_number = None
    index = 0

    for character in string:
        if character.isdigit():
            if first_number is None:
                first_number = last_number = character
            else:
                last_number = character
        for word in word_list:
            if string[index:].startswith(word):
                number=word_list.index(word)+1
                if first_number is None:
                    first_number = last_number = number
                else:
                    last_number = number
        index+=1
    answer=int(first_number)*10 + int(last_number)
    return answer


# In[98]:


SOLUTION = 0
with open('data.txt', 'r') as file:
    for row in file:
        SOLUTION += find_digits_part2(row)
print(SOLUTION)


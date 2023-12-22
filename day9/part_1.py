"""
For solving advent of code 2023 problem 9 part 1.
"""

def predict_value(row: str):
    """Given an input row, predict the next value.
    
    Notice that the predicted value for the row equals
    the sum of last elements in all arrays containing
    differences.
    
    Example: 
    Given the following list, predict the next value:
    10 13 16 21 30 45
    
    We solve this by looking at the lists containing differences.
    Notice that the solution to "?" is 45 + 23 = 68.
    The we got 23 by adding up 15 and 8. Continuing with this logic,
    we get that ? equals to 45 + 15 + 6 + 2 + 0
    which are the last elements of each array of differences.
    
    10  13  16  21  30  45  ?
       3   3   5   9  15  23
         0   2   4   6   8
           2   2   2   2
             0   0   0
    """
    prediction = 0
    list_char = row[:-1].split(' ')
    current_list = [int(number) for number in list_char]
    while not all(x == 0 for x in current_list):
        prediction += current_list[-1]
        current_list = find_differences(current_list)
    return prediction

def find_differences(input_list: list):
    """Given a list, output a list containing differences."""
    output_list = []
    for value in range(len(input_list)-1):
        output_list.append(input_list[value + 1] - input_list[value ])
    return output_list

ANSWER = 0
with open('data.txt', 'r', encoding='utf-8') as file:
    for input_row in file:
        ANSWER += predict_value(input_row)
print(ANSWER)

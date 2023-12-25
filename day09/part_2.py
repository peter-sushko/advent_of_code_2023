"""
For solving advent of code 2023 problem 9 part 2.
"""

def predict_value(row: str):
    """Given an input row, predict the preceeding value.
    
    This function calculates the preceding value for the row by analyzing the differences between 
    consecutive elements. Starting with the first element, it alternately adds and subtracts the 
    differences to compute the prediction.   
    """
    list_char = row[:-1].split(' ')
    current_list = [int(number) for number in list_char]
    prediction = current_list[0]
    count = 1
    while not all(x == 0 for x in current_list):
        current_list = find_differences(current_list)
        prediction += current_list[0] * (-1)**count
        count += 1
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

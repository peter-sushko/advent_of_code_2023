'''
For solving advent of code problem 7 part 1.
'''

from collections import Counter
import numpy as np
from scipy.stats import rankdata


def combo_score(card: str):
    '''Returns the combination score of a hand.
    
    The score is the concatenated count of the 2 most common cards.
    That is:
    combo_score of five of a kind is 50
    combo_score of four of a kind is 41
    combo_score of full house is 32
    combo_score of three of a kind is 31
    combo_score of two pair is 22
    combo_score of pair is 21
    combo_score of high card is 11
    
    Example:
    >>>combo_score('33556')
    22
    This is because we have two pair.
    '''
    char_count = Counter(card)
    most_common_chars = char_count.most_common(2)
    most_common_count = most_common_chars[0][1] if most_common_chars else 0
    second_most_common_count = most_common_chars[1][1] if len(most_common_chars) >= 2 else 0

    return int(most_common_count) * 10 + int(second_most_common_count)

def tie_break_score(card: str):
    '''Returns the tie break score of a hand.
    
    The tie break score is calculated as follows:
    value of first card times 100,000,000 plus
    value of second card times 1,000,000 plus
    value of third card times 10,000 plus
    value of fourth card times 100 plus
    value of fifth card times 1
    
    Example:
    >>>tie_break_score('AT72Q')
    1410070212
    '''
    values = {'A':14, 'K':13, 'Q':12, 'J':11, 'T':10}
    power = 4
    score = 0
    for char in card:
        if char.isdigit():
            value = int(char)
        else:
            value = values[char]
        score += value * 10 ** (2*power)
        power -=1
    return int(score)

def total_score(card:str):
    '''Calculate the total score for a given card.

    The total score is computed as 10^10 times the combo score plus the tiebreak score.
    The scoring system assigns a unique score to each card, making it possible 
    to compare hand strengths.The combo score is prioritized, focusing on combinations' 
    starting digits. This prioritization emphasizes the importance of combinations in determining 
    the hand's strength.

    Args:
        card (str): A string representing a card.

    Returns:
        int: The total score of the card. 
    '''
    return 10**10 * combo_score(card) + tie_break_score(card)

hands = []
bets = []
hand_scores = []
# The code below generates a list of hands and a list of bets.
with open('data.txt', 'r', encoding = 'utf-8') as file:
    for line in file:
        parts = line.strip().split()
        if len(parts) == 2:
            hands.append(parts[0])
            bets.append(int(parts[1]))

for hand in hands:
    hand_scores.append(total_score(hand))
# Sort the hands.
rankings =  rankdata(hand_scores, method='max').astype(int)
ANSWER = np.dot(bets,rankings) # Finally, we need pairwise product.
print(ANSWER)

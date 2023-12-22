"""
To solve problem 7 part 2 of advent of code 2023.
"""

from collections import Counter
import numpy as np
from scipy.stats import rankdata

def combo_score_part2(card: str):
    """Calculate the combination score of a hand, including the flexibility of Jacks as wildcards.

    In this scoring system, Jacks serve as flexible jokers that can substitute for any card.
    The count of Jacks is added to the count of the most common card(s) since they enhance 
    combinations. The score is determined by concatenating the counts of the two most common cards.

    - Combo Score Examples:
        - Five of a kind: 50
        - Four of a kind: 41
        - Full house: 32
        - Three of a kind: 31
        - Two pair: 22
        - Pair: 21
        - High card: 11

    Args:
        card (str): A string representing a hand of cards, including 'J' for Jacks.

    Returns:
        int: The calculated combination score for the hand.

    Example:
        >>> combo_score_part2('335J5')
        32
        This is because we have a full house.
    """

    char_count = Counter(card)
    j_count = char_count['J']
    jokerless_count = Counter(card.replace('J', ''))
    most_common_chars = jokerless_count.most_common(2)
    most_common_count = most_common_chars[0][1] if most_common_chars else 0
    second_most_common_count = most_common_chars[1][1] if len(most_common_chars) >= 2 else 0

    return int(most_common_count+j_count) * 10 + int(second_most_common_count)

def tie_break_score_part2(card: str):
    """Returns the tie break score of a hand.

    This time Jacks are jokers and their value is updated to 1.

    The tie break score is calculated as follows:
    value of first card times 100,000,000 plus
    value of second card times 1,000,000 plus
    value of third card times 10,000 plus
    value of fourth card times 100 plus
    value of fifth card times 1
    
    Example:
    >>>tie_break_score('AT72Q')
    1410070212
    
    """
    values = {'A':14, 'K':13, 'Q':12, 'J':1, 'T':10}
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
    """Calculate the total score for a given card.

    The total score is computed as 10^10 times the combo score plus the tiebreak score.
    The scoring system assigns a unique score to each card, making it possible to 
    compare hand strengths. The combo score is prioritized, focusing on combinations' 
    starting digits. This prioritization emphasizes the importance of combinations in 
    determining the hand's strength.

    Args:
        card (str): A string representing a card.

    Returns:
        int: The total score of the card.
    """
    return 10**10 * combo_score_part2(card) + tie_break_score_part2(card)

hands = []
bets = []
hand_scores = []
with open('data.txt', 'r', encoding = 'utf-8') as file:
    for line in file:
        parts = line.strip().split()
        if len(parts) == 2:
            hands.append(parts[0])
            bets.append(int(parts[1]))
for hand in hands:
    hand_scores.append(total_score(hand))
rankings =  rankdata(hand_scores, method='max').astype(int) 
ANSWER = np.dot(bets,rankings)
print(ANSWER)

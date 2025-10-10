'''
source: https://www.1point3acres.com/bbs/thread-1147946-1-1.html
You are given a deck of cards represented as an integer array deck, where each element is the value of a card. The deck may contain duplicate values.
You are also given two integers:
    k — the number of cards to draw (without replacement).
    target — the desired sum.

A player wins if the sum of the selected k cards equals target. Otherwise, the player loses.

Your task is to compute and return the probability of winning.

Examples:
Input: deck = [1, 2, 3, 4], k = 2, target = 5
Output: 0.3333
Explanation:
All possible 2-card draws:
[1,2]=3, [1,3]=4, [1,4]=5, [2,3]=5, [2,4]=6, [3,4]=7
Favorable draws = {[1,4], [2,3]} → 2 out of 6
Probability = 2/6 = 0.3333

Input: deck = [2, 2, 3], k = 2, target = 4
Output: 0.3333
Explanation:
Possible draws: [2,2]=4, [2,3]=5, [2,3]=5
Favorable draws = {[2,2]} → 1 out of 3
Probability = 1/3 = 0.3333

Constrains:
0 <= k <= 100

'''
from typing import List
from math import comb
from collections import defaultdict


# probability = combinations that satisfy the constraints / total combination
def winning_probability(k:int, target:int, deck:List[int]):
    n = len(deck)
    # dp[c][s] definition: selecting c cars and the sum is equal to s
    dp = [defaultdict(int) for _ in range(k + 1)]
    '''
    [
    {0:1}
    {}
    ]
    '''
    # initialize the dp array
    dp[0][0] = 1
    for value in deck:
        for c in range(k, 0, -1):
            for s, cnt in dp[c - 1].items():
                dp[c][s + value] += cnt
    favorable = dp[k][target]
    total = comb(n, k)
    return favorable / total

def solution() -> None:
    tests = [
        # (deck, k, target, expected_probability)
        ([1, 2, 3, 4], 2, 5, 2/6),
        ([2, 2, 3], 2, 4, 1/3),
        ([1, 2, 2, 3], 2, 4, 2/6),
        ([1, 1, 1, 1], 2, 2, 1.0),
        ([5, -1, 2, 4], 2, 3, 1/6),
        ([0, 0, 0, 0], 3, 0, 1.0),
    ]

    for i, (deck, k, target, expected) in enumerate(tests, 1):
        result = winning_probability(k, target, deck)
        print(f"Test {i}: deck={deck}, k={k}, target={target}")
        print(f"  result   = {result:.5f}")
        print(f"  expected = {expected:.5f}")
        print(f"  pass     = {abs(result - expected) < 1e-9}")
        print("-" * 40)


if __name__ == "__main__":
    solution()
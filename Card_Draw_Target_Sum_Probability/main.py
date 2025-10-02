'''
source: https://www.1point3acres.com/bbs/thread-1147946-1-1.html
遇到一道题：大概是给定一个牌堆（允许有重复的数字），再给两个输入参数：抽牌数量k，以及目标和target。
从牌堆里不放回抽出k张牌，如果它们的和等于target就算赢，否则算输。题目要求返回玩家获胜的概率。 求加米！
背包问题
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
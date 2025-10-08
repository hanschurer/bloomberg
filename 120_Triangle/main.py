from math import inf
from typing import List


class Solution:
    '''
    dp = [5, 6, inf, inf]

    prev_val = 6
    dp[j] reset to inf
    dp[j] = min(inf, 6 + 4) = 10
         11  10  13

    '''
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle[-1])
        dp = [inf] * n
        dp[0] = triangle[0][0]

        for i in range(n - 1):
            for j in range(i, -1, -1):
                prev_val = dp[j]
                dp[j] = inf
                dp[j] = min(dp[j], prev_val + triangle[i + 1][j])
                dp[j + 1] = min(dp[j + 1], prev_val + triangle[i + 1][j + 1])
        return min(dp)

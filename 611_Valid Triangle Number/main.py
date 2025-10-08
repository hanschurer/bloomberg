# https://leetcode.com/problems/valid-triangle-number/description/
from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        ans = 0
        for i in range(n):
            k = i
            for j in range(i + 1, n):
                while k + 1 < n and nums[k + 1] < nums[i] + nums[j]:
                    k += 1
                ans += max(k - j, 0)
        return ans

    '''
    类似 3-sum
    tc: O(n^2)
    sc: O(1)
    '''
    def triangleNumber2(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        nums.sort()

        for k in range(n - 1, 1, -1):
            i, j = 0, k - 1
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    res += j - i
                    j -= 1
                else:
                    i += 1
        return res


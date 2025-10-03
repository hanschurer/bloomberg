from typing import List


class Solution:
    '''
    nums  = [-1,1,0,-3,3]
    left  = [1,-1,-1,0,0]
    right = [0, 0,-9,3,1]
    '''
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [1] * n
        right = [1] * n
        for i in range(1, n):
            left[i] = left[i - 1] * nums[i - 1]
        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]

        res = []
        for i in range(n):
            res.append(left[i] * right[i])
        return res

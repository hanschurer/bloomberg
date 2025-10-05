'''
High frequent Tag problem

A peak element is an element that is strictly greater than its neighbors.
Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.
You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.
You must write an algorithm that runs in O(log n) time.
'''
from typing import List


class Solution:
    # nums[i] != nums[i + 1] for all valid i.邻居不相等
    # [1,2,3,1]
    #  L M   R
    # traverse through asending order, left close right close
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = n - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid + 1] > nums[mid]:
                left = mid + 1
            elif nums[mid] > nums[mid + 1]:
                right = mid
        # we can also return right
        return left


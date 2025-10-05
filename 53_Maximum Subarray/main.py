class Solution:
    def maxSubArray(self, nums):
        current_sum = 0
        result = nums[0]

        for num in nums:
            current_sum = max(num, current_sum + num)
            result = max(result, current_sum)
        
        return result

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [-1] * n
        stack = []

        for i in range(2 * n):
            cur = i % n
            while stack and nums[stack[-1]] < nums[cur]:
                idx = stack.pop()
                result[idx] = nums[cur]
            
            if i < n:
                stack.append(cur)
        
        return result
                

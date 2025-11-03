class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0  # left pointer of the sliding window
        zeros = 0  # count of zeros in the current window
        best = 0  # best (maximum) window length found

        for r, x in enumerate(nums):  # expand the window by moving right pointer r
            if x == 0:  
                zeros += 1 
            while zeros > k:  
                if nums[l] == 0:  
                    zeros -= 1 
                l += 1  # move left pointer right to shrink the window, eliminate 0 until valid <= k
            best = max(best, r - l + 1)  # update best with the current valid window length
        return best  
'''
TC: O(N), In worst case we might end up visiting every element of array twice, once by left pointer and once by right pointer.
Space Complexity: O(1). 
'''
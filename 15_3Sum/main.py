class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # sort the array to enable two-pointer traversal and easy duplicate skipping
        n = len(nums)  
        res: List[List[int]] = []  

        for i in range(n - 2):  # fix the first element index i; need at least two elements after it
            if i > 0 and nums[i] == nums[i - 1]:  # skip duplicate anchors to avoid duplicate triplets
                continue  

            target = -nums[i] 
            l, r = i + 1, n - 1  # initialize two pointers on the right subarray

            while l < r:  # run two-pointer sweep while pointers do not cross
                s = nums[l] + nums[r]  
                if s < target:  # if sum too small, we need a larger value, move left pointer right to increase sum
                    l += 1  
                elif s > target:  # if sum too big, we need a smaller value, move right pointer left to decrease sum
                    r -= 1  
                else:  # found a valid pair that with nums[i] sums to zero
                    res.append([nums[i], nums[l], nums[r]])  
                    lv, rv = nums[l], nums[r]  
                    while l < r and nums[l] == lv:  # skip duplicate left values, advance left pointer past duplicates
                        l += 1  
                    while l < r and nums[r] == rv:  # skip duplicate right values, retreat right pointer past duplicates
                        r -= 1  

        return res 

# TC: O(n^2) — sorting is O(n log n), outer loop for i is O(n) times, every i there is an inner two-pointer sweep O(n).

# SC: O(1) auxiliary (ignoring the output) 
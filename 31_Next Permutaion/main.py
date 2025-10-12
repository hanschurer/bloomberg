class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # [1, 3, 5, 4, 2]

        # 1) Find the pivot i (rightmost index with nums[i] < nums[i+1])
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        # after this step, nums[i+1,...n-1], i.e., [5,4,2] is non-increasing

        if i >= 0:
            # 2) Find rightmost j > i with nums[j] > nums[i]
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            # Swap to make the smallest possible increase at i
            nums[i], nums[j] = nums[j], nums[i]
            # swap 3 and 4 so that [1, 3, 5, 4, 2]->[1, 4, 5, 3, 2].

        # 3) Reverse the suffix to make it minimal increase 
        l, r = i + 1, n - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        # Reverse [5,3,2] → [2,3,5], so that [i+1, ...n-1] is the smallest combination, gives the next permutation

# tc: O(n) - one scan to find i, one scan to find j, one linear reverse
# sc: O(1) - in-place
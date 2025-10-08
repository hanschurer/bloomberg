class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def check(i: int) -> bool:
            x = nums[i]
            if x > nums[right]:
                return target > nums[right] and x >= target
            return target > nums[right] or x >= target

        left, right = -1, len(nums) - 1  )
        while left + 1 < right:  
            mid = (left + right) // 2
            if nums[mid] == nums[right]:
                right -= 1
            elif check(mid):
                right = mid
            else:
                left = mid
        return nums[right] == target

# follow up : 面试官让修改代码，从组合问题变成排序问题，

class Solution:
    def subsets(self, nums):
        result = []
        track = []

        def backtrack(start):
            # Each path reaching here is a subset (including empty set)
            result.append(track[:])  # make a shallow copy

            for i in range(start, len(nums)):
                track.append(nums[i])
                backtrack(i + 1)
                track.pop()

        backtrack(0)
        return result

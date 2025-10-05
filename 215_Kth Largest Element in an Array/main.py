from heapq import nlargest
from typing import List


class Solution:
    # Heap
    # O(N log K) time | O(K) space
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return nlargest(k, nums)[-1]

    '''
    Quick Select -- 2-way Partition, pivot is last element
    TC: O(n)
    SC: O(1)
    '''
    def findKthLargest2(self, nums: List[int], k: int) -> int:
        k = len(nums) - k

        def quick_select(l: int, r: int) -> int:
            idx = l
            for i in range(l, r):
                if nums[i] < nums[r]:
                    nums[i], nums[idx] = nums[idx], nums[i]
                    idx += 1
            nums[idx], nums[r] = nums[r], nums[idx]
            if idx > k:
                return quick_select(l, idx - 1)
            elif idx < k:
                return quick_select(idx + 1, r)
            return nums[idx]

        return quick_select(0, len(nums) - 1)


    '''
    Quick Select -- 3-way Partition
    TC: O(n)
    SC: O(1)
    '''
    def findKthLargest3(self, nums, k):
        def three_way_partition(left, right, pivot):
            lt, i, gt = left, left, right
            while i <= gt:
                # 🌟 控制如何 sort 的核心逻辑
                if nums[i] > pivot:             # Elements greater than the pivot
                    nums[lt], nums[i] = nums[i], nums[lt]
                    lt += 1
                    i += 1
                elif nums[i] < pivot:           # Elements less than the pivot
                    nums[gt], nums[i] = nums[i], nums[gt]
                    gt -= 1
                else:                           # Elements equal to the pivot
                    i += 1
            return lt, gt

        def quick_select(left, right, k_smallest):
            # Select a random pivot and partition the array
            # pivot_index = random.randint(left, right)
            pivot = nums[right]
            lt, gt = three_way_partition(left, right, pivot)

            # Check where the k-th smallest element lies
            if k_smallest < lt:     # In the "greater than pivot" region
                return quick_select(left, lt - 1, k_smallest)
            elif k_smallest > gt:   # In the "less than pivot" region
                return quick_select(gt + 1, right, k_smallest)
            return nums[lt]

        return quick_select(0, len(nums) - 1, k - 1)
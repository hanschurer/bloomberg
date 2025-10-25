from collections import Counter, defaultdict
from typing import List


class Solution:
    '''
    Bucket Sort
    Time: O(N)
    Space: O(N)
    '''
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        buckets = defaultdict(list)
        max_freq = 0
        for n, count in counts.items():
            buckets[count].append(n)
            max_freq = max(max_freq, count)

        res = []
        for i in range(max_freq, -1, -1):
            res.extend(buckets[i])
            if len(res) == k:
                break
        return res
    
    '''
    Quick Select
    Average Time: O(N)
    Space: O(N)
    '''
    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        n_nums = list(counts.keys())

        def q_select(nums, l, r) -> None:
            if l >= r:
                return
            idx = l
            for i in range(l, r):
                if counts[nums[i]] > counts[nums[r]]:
                    nums[i], nums[idx] = nums[idx], nums[i]
                    idx += 1
            nums[idx], nums[r] = nums[r], nums[idx]

            if idx > k:
                q_select(nums, l, idx - 1)
            elif idx < k:
                q_select(nums, idx + 1, r)

        q_select(n_nums, 0, len(n_nums) - 1)
        return n_nums[:k]

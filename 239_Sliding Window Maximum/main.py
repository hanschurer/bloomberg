from collections import deque
from heapq import heappop, heappush
from typing import List


class Solution:
    '''
    Priority Queue
    '''
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_heap, res = [], []
        for i, num in enumerate(nums):
            while max_heap and max_heap[0][1] < i - k + 1:
                heappop(max_heap)
            #                 num  index
            heappush(max_heap, (-num, i))
            if i - k + 1 >= 0:
                res.append(-max_heap[0][0])
        return res

    '''
    Deque
    nums = [1,3,-1,-3,5,3,6,7], k = 3
    deque = [(3, 1), (-1, 2)]
          大                 小
    popleft: idx < i - k + 1
    pop: prev_val < curr_val
    '''
    def maxSlidingWindow2(self, nums: List[int], k: int) -> List[int]:
        dq = deque([])
        res = []
        for i, num in enumerate(nums):
            # 检查 valid index
            while dq and dq[0][1] < i - k + 1:
                dq.popleft()
            # 检查最大值
            while dq and dq[-1][0] < num:
                dq.pop()
            dq.append((num, i))
            if i - k + 1 >= 0:
                res.append(dq[0][0])
        return res

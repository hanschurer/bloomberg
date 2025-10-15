# Definition for singly-linked list.
from typing import List, Optional
from heapq import *


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    '''
    Heap
    tc: O(nlogn)
    sc: O(n)
    '''
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ListNode.__lt__ = lambda a, b: a.val < b.val
        min_h = [head for head in lists if head]
        heapify(min_h)

        dummy = curr = ListNode(-1)
        while min_h:
            node = heappop(min_h)
            curr.next = node
            curr = curr.next
            if node.next:
                heappush(min_h, node.next)
        return dummy.next


    '''
    Divide and Conquer (Similar to Merge Sort)
    tc: O(nlogn)
    sc: O(logn)
    '''
    def mergeKLists2(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        return self._helper(lists, 0, len(lists))

    def _helper(self, lists: List[Optional[ListNode]], i: int, j: int) -> Optional[ListNode]:
        n = j - i

        def merge_two_lists(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
            dummy = curr = ListNode()
            while l1 and l2:
                if l1.val < l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next
            curr.next = l1 if l1 else l2
            return dummy.next

        if n == 0:
            return None
        elif n == 1:
            return lists[i]
        left = self._helper(lists, i, i + n // 2)
        right = self._helper(lists, i + n // 2, j)
        return merge_two_lists(left, right)


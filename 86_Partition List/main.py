# Definition for singly-linked list.

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        l1_dummy, l2_dummy = ListNode(), ListNode()
        small, big, cur = l1_dummy, l2_dummy, head

        while cur:
            if cur.val < x:
                small.next = cur
                small = small.next
            else:
                big.next = cur
                big = big.next
            cur = cur.next

        small.next = l2_dummy.next
        big.next = None
        return l1_dummy.next

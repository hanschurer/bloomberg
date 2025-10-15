# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cnt = 0
        curr = head
        while curr:
            cnt += 1
            curr = curr.next

        target = cnt - n
        dummy = curr = ListNode(-1)
        curr.next = head
        for _ in range(target):
            curr = curr.next
        curr.next = curr.next.next
        return dummy.next

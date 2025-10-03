#https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/description/?envType=company&envId=bloomberg&favoriteSlug=bloomberg-thirty-days
from typing import Optional


class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

# 递归 O(n), O(n)

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        self.dfs(head)
        return head

    def dfs(self, head):
        last = head

        while head:
            if not head.child:
                last = head
                head = head.next

            else:
                tmp = head.next
                childLast = self.dfs(head.child)
                head.next = head.child
                head.child.prev = head
                head.child = None

                if childLast: childLast.next = tmp
                if tmp: tmp.prev = childLast

                last = head
                head = childLast

        return last

# 迭代 O(n), O(1)
    def flatten2(self, head: Optional[Node]) -> Optional[Node]:
        if not head:
            return
        dummy_head = Node(-1)
        curr = dummy_head
        st = [head]
        while st:
            node = st.pop()
            curr.next = node
            node.prev = curr
            curr = curr.next
            if node.next:
                st.append(node.next)
            if node.child:
                st.append(node.child)
                node.child = None
        dummy_head.next.prev = None
        return dummy_head.next


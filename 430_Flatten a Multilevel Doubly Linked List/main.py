#https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/description/?envType=company&envId=bloomberg&favoriteSlug=bloomberg-thirty-days


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

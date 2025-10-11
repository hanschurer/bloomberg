'''
source：微信群新建面经
116. Populating Next Right Pointers in Each Node

You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.
'''

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return 
        q = deque([root])

        while q:
            pre = None
            for _ in range(len(q)):
                node = q.popleft()
                if pre:
                    pre.next = node
                pre = node
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return root

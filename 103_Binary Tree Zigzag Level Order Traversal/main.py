from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        res, dq, reverse = [], deque([root]), False

        while dq:
            level = []
            for _ in range(len(dq)):
                if not reverse:
                    node = dq.popleft()
                    level.append(node.val)
                    if node.left: dq.append(node.left)
                    if node.right: dq.append(node.right)
                else:
                    node = dq.pop()
                    level.append(node.val)
                    if node.right: dq.appendleft(node.right)
                    if node.left: dq.appendleft(node.left)
            res.append(level)
            reverse = not reverse
        return res

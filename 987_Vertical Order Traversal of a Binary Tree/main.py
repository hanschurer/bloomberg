"""
原題。
"""
from collections import defaultdict, deque
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # DFS
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        col_nodes = defaultdict(list)

        def dfs(node: TreeNode, row: int, col: int) -> None:
            if not node:
                return
            col_nodes[col].append((row, node.val))
            dfs(node.left, row + 1, col - 1)
            dfs(node.right, row + 1, col + 1)

        dfs(root, 0, 0)
        return [[val for _, val in sorted(nodes)] for _, nodes in sorted(col_nodes.items())]

    # BFS
    def verticalTraversal2(self, root: Optional[TreeNode]) -> List[List[int]]:
        col_nodes = defaultdict(lambda: [])
        min_col, max_col = float('inf'), float('-inf')
        q = deque([(root, 0)])
        while q:
            size = len(q)
            while size > 0:
                node, col = q.popleft()
                col_nodes[col].append(node.val)
                min_col = min(col, min_col)
                max_col = max(col, max_col)
                if node.left:
                    q.append((node.left, col - 1))
                if node.right:
                    q.append((node.right, col + 1))
                size -= 1
        return [sorted(col_nodes[i]) for i in range(min_col, max_col + 1)]

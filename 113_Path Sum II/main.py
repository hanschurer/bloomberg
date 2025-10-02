# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        def dfs(node: TreeNode, cur_sum: int) -> None:
            if node is None:
                return
            cur_sum += node.val
            curr.append(node.val)
            if not node.left and not node.right and cur_sum == targetSum:
                res.append([*curr])
            dfs(node.left, cur_sum)
            dfs(node.right, cur_sum)
            curr.pop()

        res, curr = [], []
        dfs(root, 0)
        return res

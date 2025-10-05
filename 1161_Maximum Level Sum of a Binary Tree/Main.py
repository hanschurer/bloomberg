'''
source: https://www.xiaohongshu.com/explore/68e046a5000000000700c6ed?app_platform=ios&app_version=9.3.1&share_from_user_hidden=true&xsec_source=app_share&type=normal&xsec_token=CB9EJWt5qEzdbGv5Y6tcYFeu6RkChW6VYt4TJqQMamHMc=&author_share=1&xhsshare=WeixinSession&shareRedId=N0k4NkVLNjo2NzUyOTgwNjczOTo0RkpC&apptime=1759530496&share_id=bf29fe0a02e342feb23979d30404a864
similar question
Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

BFS + counting
'''
from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_level = 0
        max_sum = float('-inf')
        queue = deque([root])
        level = 0
        while queue:
            level_sum = 0
            level += 1
            for i in range(len(queue)):
                cur = queue.popleft()
                level_sum += cur.val
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            if level_sum > max_sum:
                max_sum = level_sum
                max_level = level
        return max_level


# ---------- Unit Test ----------
def build_tree(values):
    """Helper: build tree from level-order list (None for missing nodes)."""
    if not values:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    root1 = build_tree([1,7,0,7,-8,None,None])
    print("Test 1 Expected=2, Got=", sol.maxLevelSum(root1))

    # Example 2
    root2 = build_tree([989,None,10250,98693,-89388,None,None,None,-32127])
    print("Test 2 Expected=2, Got=", sol.maxLevelSum(root2))

    # Custom test: single node
    root3 = build_tree([5])
    print("Test 3 Expected=1, Got=", sol.maxLevelSum(root3))

    # Custom test: skewed tree
    root4 = build_tree([1,2,None,3,None,4,None])
    print("Test 4 Expected=4, Got=", sol.maxLevelSum(root4))

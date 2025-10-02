'''
Source: https://leetcode.com/discuss/post/1125587/bloomberg-interview-question-by-kaleungt-am7w/
Question:
You are given the root of a binary tree where each node has a value in the range [0, 25] representing the letters 'a' to 'z'.
Return the lexicographically smallest string that starts at a leaf of this tree and ends at the root.
As a reminder, any shorter prefix of a string is lexicographically smaller.
For example, "ab" is lexicographically smaller than "aba".

A leaf of a node is a node that has no children.

- The number of nodes in the tree is in the range [1, 8500].
- 0 <= Node.val <= 25
'''
from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        '''
        depth first search: maintain a current smallest string
        '''
        min_string = None
        def dfs(node, cur_string):
            nonlocal min_string
            cur_char = chr(ord('a') + node.val)
            cur_string = cur_char + cur_string
            # leaf node
            if not node.left and not node.right:
                if not min_string or min_string > cur_string:
                    min_string = cur_string
                return
            if node.left:
                dfs(node.left, cur_string)
            if node.right:
                dfs(node.right, cur_string)
            return
        dfs(root, '')
        return min_string
def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root

def main():
    tests = [
        ([0,1,2,3,4,3,4], "dba"),   # 预期结果来自 LeetCode 示例
        ([25,1,3,1,3,0,2], "adz"),
        ([2,2,1,None,1,0,None,0], "abc")
    ]
    sol = Solution()
    for i, (arr, expected) in enumerate(tests, 1):
        root = build_tree(arr)
        result = sol.smallestFromLeaf(root)
        print(f"Test {i}: result = {result}, expected = {expected}, pass = {result == expected}")

if __name__ == "__main__":
    main()
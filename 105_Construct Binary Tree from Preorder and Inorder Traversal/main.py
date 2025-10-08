'''
lc tag
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.


'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {num: i for i, num in enumerate(inorder)}
        self.pre_idx = 0

        def helper(in_left, in_right):
            if in_left > in_right:
                return None
            val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(val)

            split = inorder_map[val]
            root.left = helper(in_left, split - 1)
            root.right = helper(split + 1, in_right)
            return root

        return helper(0, len(inorder) - 1)

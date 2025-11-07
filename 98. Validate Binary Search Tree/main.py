# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        pre = - inf

        def dfs(root):
            nonlocal pre
            if not root: return True
            if not dfs(root.left):
                return False
            if pre >= root.val:
                return False
            pre = root.val
            return dfs(root.right)
        
        return dfs(root)
    

# follow-up in phone screen: Time complexity O(n): 
#                           interviewer asked is this the best case or worst case time complexity
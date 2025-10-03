

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ant=[]
        q=deque([root])
        while q:
            vals=[]
            for _ in range(len(q)):
                node= q.popleft()
                vals.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            ant.append(vals)
           
        return ant
           

#test case 1: root=[]
#test case 2: root=[1]
#test case 3: root=[3,9,20,null,null,15,7]

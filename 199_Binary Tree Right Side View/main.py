class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def dfs(node: Optional[TreeNode], depth: int) -> None:
            if node is None:
                return
            if depth == len(ans):  
                ans.append(node.val)
            dfs(node.right, depth + 1)  
            dfs(node.left, depth + 1)
        dfs(root, 0)
        return ans


'''
题目是从二叉树decrypt出string。比如
     i
    / \
   r   e
  / \
 p   c
按列从上到下遍历，就是p r i c e。要注意的是e如果有left child也会在c的位置，而不会让整个right subtree向右移。在这儿卡了好久，面试官提示讲清楚了树结构。然后就是tree level traversal了，用bfs遍历，存到unordered map里，最后复原。但本人tree level traversal刷题时用的递归+zip，这里不太合适，几经面试官提示下手撕bfs解法，现在懊悔不已

'''
from typing import Optional, List


class TreeNode:
    def __init__(self, val: str) -> None:
        self.val = val
        self.left = None
        self.right = None

def build_tree(idx: int, arr: List[str]) -> Optional[TreeNode]:
    if idx >= len(arr) or not arr[idx]:
        return None
    root = TreeNode(arr[idx])
    root.left = build_tree(idx * 2 + 1, arr)
    root.right = build_tree(idx * 2 + 2, arr)
    return root

def decrypt(root: TreeNode) -> str:
    pos = {}

    def dfs(node: TreeNode, r: int, c: int) -> None:
        if not node:
            return
        pos[(c, r)] = node.val
        dfs(node.left, r + 1, c - 1)
        dfs(node.right, r + 1, c + 1)

    dfs(root, 0, 0)
    return "".join(c for _, c in sorted(pos.items()))


'''
     i
    / \
   r   e
  / \
 p   c
'''
vals = ['i', 'r', 'e', 'p', 'c']
root = build_tree(0, vals)
print(decrypt(root))  # 'price'

'''
     i
    / \
   r   e
  /   /
 p   c
'''
vals = ['i', 'r', 'e', 'p', None, 'c']
root = build_tree(0, vals)
print(decrypt(root))  # 'price'

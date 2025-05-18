from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root, depth):
            nonlocal res
            if not root:
                return depth
            
            left_depth = dfs(root.left, depth)
            right_depth = dfs(root.right, depth)
            res = max(res, left_depth + right_depth)
            return max(right_depth, left_depth) + 1
        
        dfs(root, 0)
        return res
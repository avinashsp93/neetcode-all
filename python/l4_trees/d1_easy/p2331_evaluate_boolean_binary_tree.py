# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def dfs(n):
            if n.val == 0:
                return False
            elif n.val == 1:
                return True
            elif n.val == 2:
                return dfs(n.left) or dfs(n.right)
            elif n.val == 3:
                return dfs(n.left) and dfs(n.right)
        return dfs(root)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Using global rangeSum (rangeSum as property)
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:     
        def dfs(root):
            if not root:
                return 0
            if root.val > high:
                return dfs(root.left)
            elif root.val < low:
                return dfs(root.right)
            else:
                return root.val + dfs(root.left) + dfs(root.right)
        return dfs(root)
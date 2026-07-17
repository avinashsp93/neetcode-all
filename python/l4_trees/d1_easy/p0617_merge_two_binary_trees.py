# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(r1, r2):
            if r1 is None and r2 is None:
                return
            elif r1 is None:
                return TreeNode(r2.val, dfs(r2.left, None), dfs(r2.right, None))
            elif r2 is None:
                return TreeNode(r1.val, dfs(r1.left, None), dfs(r1.right, None))
            else:
                return TreeNode(r1.val + r2.val, dfs(r1.left, r2.left), dfs(r1.right, r2.right))

        return dfs(root1, root2)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root, runningSum):
            if not root:
                return False
            runningSum += root.val
            if root.left is None and root.right is None:
                if runningSum == targetSum:
                    return True
                else:
                    return False
            return dfs(root.left, runningSum) or dfs(root.right, runningSum)
        return dfs(root, 0)
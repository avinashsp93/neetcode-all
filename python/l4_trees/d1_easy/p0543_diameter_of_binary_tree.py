# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    maxDiameter = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def calculateDiameter(node):
            if node is None:
                return 0
            leftHeight = calculateDiameter(node.left)
            rightHeight = calculateDiameter(node.right)
            self.maxDiameter = max(self.maxDiameter, leftHeight + rightHeight)
            return max(leftHeight, rightHeight) + 1
        calculateDiameter(root)
        return self.maxDiameter
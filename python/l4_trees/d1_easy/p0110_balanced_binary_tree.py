# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def getHeightAndBalance(node):
            if node == None:
                return [True, 0]
            leftBalanceAndHeight = getHeightAndBalance(node.left)
            rightBalanceAndHeight = getHeightAndBalance(node.right)
            
            balanced = leftBalanceAndHeight[0] and rightBalanceAndHeight[0] and abs(rightBalanceAndHeight[1] - leftBalanceAndHeight[1]) <= 1
            return [balanced, max(leftBalanceAndHeight[1], rightBalanceAndHeight[1]) + 1]
        
        finalBalanceAndHeight = getHeightAndBalance(root)
        return finalBalanceAndHeight[0]
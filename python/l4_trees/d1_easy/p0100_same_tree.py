# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # recursive
        def preorderComparison(r1, r2):
            # when both roots are empty
            if not r1 and not r2:
                return True
            
            # when either one of them are empty, because both being empty is handled above
            # or none of them are empty with them having unequal values
            if not r1 or not r2 or r1.val != r2.val:
                return False
            
            # recursive call
            return preorderComparison(r1.left, r2.left) and preorderComparison(r1.right, r2.right)

        return preorderComparison(p, q)
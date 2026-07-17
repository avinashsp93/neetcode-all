# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def mirror(r1, r2):
            if not r1 and not r2:
                return True
            elif not r1 or not r2:
                return False
            else:
                if r1.val != r2.val:
                    return False
                return mirror(r1.left, r2.right) and mirror(r1.right, r2.left)
        if root:
            return mirror(root.left, root.right)
        return True


    # def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    #     r1 = root
    #     r2 = root
    #     resInOrder = []
    #     resInOrderRev = []

    #     def inorder(root):
    #         if not root:
    #             return
    #         inorder(root.left)
    #         resInOrder.append(root.val)
    #         inorder(root.right)
    #     inorder(r1)

    #     def inorderReversal(root):
    #         if not root:
    #             return
    #         inorderReversal(root.right)
    #         resInOrderRev.append(root.val)
    #         inorderReversal(root.left)
    #     inorderReversal(r2)

    #     if len(resInOrder) == len(resInOrderRev):
    #         for i in range(0, len(resInOrder)):
    #             if(resInOrder[i] != resInOrderRev[i]):
    #                 return False
    #         return True
    #     return False
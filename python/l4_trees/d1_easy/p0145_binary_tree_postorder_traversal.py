# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # recursive

        result = []

        def postorder(root):
            if not root:
                return
            postorder(root.left)
            postorder(root.right)
            result.append(root.val)

        postorder(root)
        return result
    
    def postorderTraversalIterative(self, root: Optional[TreeNode]) -> List[int]:
        # iterative

        result = []
        stack = []

        curr = root
        while curr or stack:
            while curr:
                stack.append(curr.right)
                curr = curr.left
            if curr:
                result.append(curr.val)
            else:
                curr = stack.pop()

        return result
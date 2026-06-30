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

        stack = [root]
        visited = [False]

        result = []

        while stack:
            cur = stack.pop()
            vis = visited.pop()

            if cur:
                if vis:
                    result.append(cur.val)
                else:
                    stack.append(cur)
                    visited.append(True)
                    stack.append(cur.right)
                    visited.append(False)
                    stack.append(cur.left)
                    visited.append(False)
            return result
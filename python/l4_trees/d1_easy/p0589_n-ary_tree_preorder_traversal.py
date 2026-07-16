"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        result = []
        def nary_preorder_recursive(root):
            if not root:
                return
            result.append(root.val)
            for i in root.children:
                nary_preorder_recursive(i)

        nary_preorder_recursive(root)
        return result
"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        result = []

        def nary_postorder(root):
            if not root:
                return
            for i in root.children:
                nary_postorder(i)
            result.append(root.val)

        nary_postorder(root)
        return result
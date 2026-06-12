# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Solution using HashSet O(n) memory
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        linkSet = set()
        currA, currB = headA, headB
        while currA:
            linkSet.add(currA)
            currA = currA.next

        while currB:
            if currB in linkSet:
                return currB
            currB = currB.next
        
        return None
        
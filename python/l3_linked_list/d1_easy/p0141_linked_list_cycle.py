class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        curr = head
        linkValueSet = set()
        while curr is not None:
            if curr in linkValueSet:
                return True
            linkValueSet.add(curr)
            curr = curr.next 
        return False
    
    def hasCycle_floydsTortoiseAndHare(self, head: ListNode) -> bool:
        tortoise, hare = head, head
        while hare is not None and hare.next is not None:
            tortoise = tortoise.next
            hare = hare.next.next
            if tortoise == hare:
                return True
        return False

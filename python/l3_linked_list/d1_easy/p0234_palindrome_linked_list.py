# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        tortoise,hare,start = head,head,head
        
        while hare is not None and hare.next is not None:
            tortoise = tortoise.next
            hare = hare.next.next

        prev = None
        while tortoise is not None:
            nxt = tortoise.next
            tortoise.next = prev
            prev = tortoise
            tortoise = nxt

        end = prev

        while end is not None:
            if start.val != end.val:
                return False
            start = start.next
            end = end.next
        return True
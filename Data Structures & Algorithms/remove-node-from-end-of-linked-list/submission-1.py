# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None:
            return None

        prev = None
        h = head
        c = 1

        while h.next:
            c += 1
            h = h.next

        k = c - n

        if k == 0:
            return head.next

        curr = head
        s = 1

        while s <= k:
            prev = curr
            curr = curr.next
            s += 1
        
        prev.next = curr.next
        curr.next = None
        return head
        
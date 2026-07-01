# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if head.next is None:
            return

        #find half
        s = head
        f = head.next
        while f is not None and f.next is not None:
            f = f.next.next
            s = s.next
        
        head2 = s.next
        s.next = None

        #reverse 2nd part
        prev = None
        h = head2
        while h:
            t = h.next
            h.next = prev
            prev = h
            h = t
        head2 = prev

        #merge
        res = head
        while head and head2:
            t = head.next
            p = head2.next

            head.next = head2
            head2.next = t
            head2 = p
            head = t

        
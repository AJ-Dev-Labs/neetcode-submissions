# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        head1 = l1
        head2 = l2

        # form number a
        p = 0
        d = 0
        while head1:
            d = d + (head1.val * (10**p))
            head1 = head1.next
            p += 1
        a = d

        # form number b
        d = 0
        p = 0
        while head2:
            d = d + (head2.val * (10**p))
            head2 = head2.next
            p += 1
        b = d

        # add nums
        s = a + b

        # traverse Sum to form nodes
        nNext = ListNode(s%10)
        res = nNext
        s = s // 10
        while(s != 0):
            dig = s % 10
            curr = ListNode(dig)
            nNext.next = curr
            nNext = curr
            s = s // 10
        return res
        
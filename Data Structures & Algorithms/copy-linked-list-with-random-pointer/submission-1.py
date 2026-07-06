"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return None
        nodeMap = {}

        t = head
        t1 = head
        while head:
            n = Node(head.val)
            nodeMap[head] = n
            head = head.next
        
        while t:
            n = nodeMap[t]
            if t.next:
                n.next = nodeMap[t.next]
            else:
                n.next = None
            if t.random:
                n.random = nodeMap[t.random]
            else:
                n.random = None
            t = t.next
        return nodeMap[t1]

        
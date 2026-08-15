# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if not p and not q:
            return True
        elif not p and q:
            return False
        elif p and not q:
            return False

        deq1 = deque([p])
        deq2 = deque([q])

        while deq1 and deq2:
            root1 = deq1.popleft()
            root2 = deq2.popleft()

            if root1 and root2:
                if root1.val != root2.val:
                    return False
            else:
                return False
            
            if root1.left and root2.left:
                deq1.append(root1.left)
                deq2.append(root2.left)
            elif root1.left and not root2.left:
                return False
            elif not root1.left and root2.left:
                return False
            
            if root1.right and root2.right:
                deq1.append(root1.right)
                deq2.append(root2.right)
            elif root1.right and not root2.right:
                return False
            elif not root1.right and root2.right:
                return False

            
        
        if deq1 or deq2:
            return False
        else:
            return True
        
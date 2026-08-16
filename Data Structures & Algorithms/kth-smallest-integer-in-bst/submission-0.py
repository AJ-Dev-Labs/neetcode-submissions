# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        res = []

        def inOrder(node, temp):
            if not node:
                return
            
            inOrder(node.left, temp)
            temp.append(node.val)
            inOrder(node.right, temp)
        
        inOrder(root, res)

        idx = k-1
        return res[idx]
        
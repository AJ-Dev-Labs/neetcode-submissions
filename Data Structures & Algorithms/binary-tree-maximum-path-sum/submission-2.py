# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        res = float("-inf")

        def path(node):
            nonlocal res
            if not node:
                return 0
            
            if not node.left and not node.right:
                res = max(res, node.val)
                return node.val 
            
            left = path(node.left)
            right = path(node.right)
            left = max(left, 0)
            right = max(right, 0)
            pathSum = node.val+left+right
            res = max(res, pathSum)
            
            sumNode = node.val + max(left, right)
            
            return sumNode
        a = path(root)
        res = max(a, res)
        return res

        
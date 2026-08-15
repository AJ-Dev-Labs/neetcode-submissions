# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []

        deq = deque([root])

        while deq:
            len_q = len(deq)
            temp = []
            for i in range(len_q):
                node = deq.popleft()
                temp.append(node.val)

                if node.left:
                    deq.append(node.left)
                if node.right:
                    deq.append(node.right)
                
            res.append(temp)
        return res

        
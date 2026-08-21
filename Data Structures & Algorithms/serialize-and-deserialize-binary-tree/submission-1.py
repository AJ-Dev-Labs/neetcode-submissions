# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        result = []

        def serialHelper(node):
            if not node:
                result.append("null")
                return
            result.append(str(node.val))
            serialHelper(node.left)
            serialHelper(node.right)
        serialHelper(root)
        return ",".join(result)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        nodes = data.split(",")
        idx = 0
        def deserialHelper():
            nonlocal idx
            if(idx >= len(nodes)):
                return None
            val = nodes[idx]
            idx +=1
            if(val == "null"):
                return None
            n = TreeNode(val)
            n.left = deserialHelper()
            n.right = deserialHelper()
            return n
        return deserialHelper()

            

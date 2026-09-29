# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        q = collections.deque([root])

        while q:
            c = q.popleft()

            if not c:
                res.append(None)
            else:
                res.append(c.val)
                q.append(c.left)
                q.append(c.right)

        while res and res[-1] is None:
            res.pop()
        
        for i in range(len(res)): 
            if res[i] is None:
                res[i] = "#"
        
        s = ".".join(str(x) for x in res)

        return s
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        
        l = data.split(".") 

        root = TreeNode(int(l[0]))
        q = collections.deque([root])
        i = 1
        n = len(l)

        while q and i < n:
            p = q.popleft()

            if i < n and l[i] != "#":
                p.left = TreeNode(int(l[i]))
                q.append(p.left)
            i += 1
        
            if i < n and l[i] != "#":
                p.right = TreeNode(int(l[i]))
                q.append(p.right)
            i += 1
        
        return root


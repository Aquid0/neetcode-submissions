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
        q = collections.deque([root])

        while q: 
            level = len(q)
            curr = []
        
            for i in range(level):
                c = q.popleft()
                curr.append(c.val)

                if c.left: q.append(c.left)
                if c.right: q.append(c.right)
            
            res.append(curr)
            curr = []
        
        return res
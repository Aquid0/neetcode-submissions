# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isEqual(f, g):
            if not f and not g:
                return True
            elif not f or not g or f.val != g.val:
                return False
            else:
                return isEqual(f.left, g.left) and isEqual(f.right, g.right)

        q = collections.deque([root])
        c = None

        while q:
            c = q.popleft()
            if c.val == subRoot.val: 
                if isEqual(c, subRoot):
                    return True
            if c.left: q.append(c.left)
            if c.right: q.append(c.right)
        
        return False
            
            

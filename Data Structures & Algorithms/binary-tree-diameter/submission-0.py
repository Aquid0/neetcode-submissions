# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def f(c):
            if not c:
                return 0
            
            l = f(c.left)
            r = f(c.right)
            self.ans = max(self.ans, l + r)
            
            return 1 + max(l, r)
        
        f(root)

        return self.ans 


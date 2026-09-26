# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.ans = True
        def f(c):
            if not c:
                return 0
            
            l = f(c.left)
            r = f(c.right)
            if abs(r - l) > 1:
                self.ans = False
            
            return 1 + max(l, r)
        
        f(root)

        return self.ans
        
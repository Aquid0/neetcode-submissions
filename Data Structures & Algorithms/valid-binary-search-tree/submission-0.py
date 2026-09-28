# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        self.track = []
        def dfs(node):
            if not node:
                return
            
            dfs(node.left)

            self.track.append(node.val)
        
            dfs(node.right)

        dfs(root)

        for i in range(1, len(self.track)):
            if self.track[i] <= self.track[i-1]:
                return False
        
        return True
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        self.ans = 0
        
        def dfs(node, currMax):
            # current node is greater than the current max of the path to get to this node
            if node.val >= currMax:
                self.ans += 1
                currMax = node.val
            
            if node.left:
                dfs(node.left, currMax)
            if node.right: 
                dfs(node.right, currMax)
        
        dfs(root, float('-inf'))

        return self.ans
                


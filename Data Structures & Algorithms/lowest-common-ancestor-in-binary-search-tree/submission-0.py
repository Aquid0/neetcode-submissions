# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.h = {}    

        def f(node, target):
            if not node: 
                return False
            
            l_found = f(node.left, target)
            r_found = f(node.right, target)
            found = node == target or l_found or r_found
        
            if node not in self.h: 
                self.h[node] = [found]
            else: 
                self.h[node].append(found)
            
            return found

        def g(node):
            if not node:
                return None
            
            q = collections.deque([node])
            deepest_match = None

            while q: 
                node = q.popleft()

                if self.h[node] == [True, True]:
                    deepest_match = node
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            return deepest_match

        f(root, p)
        f(root, q)
        ans = g(root)

        return ans 

            

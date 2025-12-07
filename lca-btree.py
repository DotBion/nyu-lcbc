# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = 0
        def dfs(node):
            if not node:
                return False
            left = dfs(node.left)
            right = dfs(node.right)
            
            if (node == p or node == q) and (left or right):
                nonlocal ans
                ans = node
                return True
            elif left and right:
                ans = node
            elif (node == p or node == q):
                return True
            return left or right
        
        dfs(root)
        return ans
                
            
        
        

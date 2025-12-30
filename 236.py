# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def solve(root, p, q):
            if not root:
                return None
            elif root == p:
                return p
            elif root == q:
                return q
            
            left = solve(root.left, p, q)
            right = solve(root.right, p, q)

            if left and right:
                return root
            elif left:
                return left
            elif right:
                return right
        
        return solve(root, p, q)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # track leaves for tree1
        leaf1 = []
        leaf2 = []
        # track leaveds for tee2
        #breadth first search, if leaf, add the node value to the respective tracker
        # will need to use recursion
        # base case is if there is no more root, maybe also no root.next?
        def dfs(root, tracker):
            if not root:
                return
            if root.left == None and root.right == None:
                tracker.append(root.val)
            else:
                dfs(root.left, tracker)
                dfs(root.right, tracker)
        dfs(root1, leaf1)
        dfs(root2, leaf2)
        if leaf1 == leaf2:
            return True
        
        return False



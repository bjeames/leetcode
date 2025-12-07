# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # keep track of path
        # if current node is >=  to all nodes in path, increment counter
        if not root:
            return 0
        
        counter = 0
        queue = deque([(root, root.val)])

        while queue:
            level_len = len(queue)
            for _ in range(level_len):
                node, max_val = queue.popleft()
                if node.val >= max_val:
                    counter +=1
                if node.left:
                    queue.append([node.left, max(node.val, max_val)])
                if node.right:
                    queue.append([node.right, max(node.val, max_val)])

        return counter

            










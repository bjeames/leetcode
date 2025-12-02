# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # We want the furthest right node of each level
        # make a queue for each level, but only append the last node to the result list
        if not root:
            return []
        queue = deque([root])
        res = []
        while queue:
            current_level_len = len(queue)
            furthest_right = None
            for _ in range(current_level_len):
                current_node = queue.popleft()
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
                furthest_right = current_node.val
            
            res.append(furthest_right)
        return res

        
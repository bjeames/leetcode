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
    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = deque([root])
        res = []
        while queue:
            cur_lvl = []
            for i in range(len(queue)):
                cur_node = queue.popleft()
                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)
                cur_lvl.append(cur_node.val)

            res.append(cur_lvl[-1])
        return res



        

        
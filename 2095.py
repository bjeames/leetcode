# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # save the head
        # find the length of the linked list
        # 3//2 = 1
        # 4//2 = 2  
        # iterate through the linked list until the node 1 short of the middle
        # point that node and the node after middle

        head = head
        current_node = head
        list_len = 0
        
        while current_node:
            list_len += 1
            current_node = current_node.next
        target = (list_len//2) - 1

        if list_len == 0 or list_len == 1:
            return None

        current_node = head
        for _ in range(target):
            current_node = current_node.next
        
        current_node.next = current_node.next.next

        return head



            


        
        
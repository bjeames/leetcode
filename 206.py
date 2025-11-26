# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # make sure there is a head, if not return head
        if not head:
            return head
        # make a place holder for previous node, start as None
        previous = None
        # start current node as head
        current = head 

        # iterate over each node with a while loop, until current = None
        while current:
        # save the current nodes next node, so you can errase currents pointer
            next_node = current.next
        # point the current node at previous node, i.e. reverse its pointer
            current.next = previous
        # move the previous node up 1 by making it the current node
            previous = current
        # update current as the next node you saved at the beginning of the loop
            current = next_node
        
        # return previous because the while loop will stop once current = None, and 
        # at that point you need to return the node the came before it (previous) which
        # is the new head.
        return previous
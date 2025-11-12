# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head # make starting point
        previous = None # track previous

        while current:
            next = current.next # save the next node before reassigning current nodes pointer
            current.next = previous # set current nodes pointer at the previous node
            previous = current # move previous node up before moving up current node
            current = next # move current node up to node saved at the beginning of the iteration
        
        return previous # the iteration stops once current = None, so return the node before that
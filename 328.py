# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # is the list only one or two items? If so, already in format we want
        if not head or not head.next:
            return head
        # track the current odd node
        odd = head
        # track the current even node
        even = head.next
        # save the even head, dont do it for odd bc we don't modify head
        even_head = even

        # is there and even node a node that comes after?
        while even and even.next:
            # already saved odd's original next node with even
            odd.next = even.next
            # move odd pointer forward
            odd = odd.next

            # reset even's pointer to the node after the odd
            even.next = odd.next
            # move even up
            even = even.next
        
        odd.next = even_head

        return head

                    

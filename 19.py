# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        k = 0
        curr = head
        while curr:
            k+=1
            curr = curr.next
        if n == k:
            return head.next
        i = k-n-1
        curr = head
        for _ in range(i):
            curr = curr.next

        curr.next = curr.next.next

        return head
            
        
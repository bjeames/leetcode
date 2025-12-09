# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # find the length of the list
        # go up to the middle node, reverse everything past it
        # go through each list, compute max and compare it to a tracker max
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next

        sec_head = head
        for _ in range(n//2):
            sec_head = sec_head.next
        
        previous = None
        curr_2 = sec_head

        while curr_2:
            next_node = curr_2.next
            curr_2.next = previous
            previous = curr_2
            curr_2 = next_node

        global_max = 0

        while previous:
             global_max = max(global_max, head.val + previous.val)
             head = head.next
             previous = previous.next

        return global_max

        

        
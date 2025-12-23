# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # helper function to reverse lists
        # for each list, make a integer string
        # convert to the strings to ints and add them together
        # convert the int back to a str
        # iterate over each digit to make the output linked list
        def reverse_list(head):
            curr = head
            prev = None
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev
        l1_reversed = reverse_list(l1)
        l1_string = ''
        l2_reversed = reverse_list(l2)
        l2_string = ''
        while l1_reversed:
            l1_string += str(l1_reversed.val)
            l1_reversed = l1_reversed.next
        while l2_reversed:
            l2_string += str(l2_reversed.val)
            l2_reversed = l2_reversed.next
        res_str = str(int(l1_string) + int(l2_string))
        dummy = ListNode()
        curr = dummy
        for d in res_str:
            curr.next = ListNode(int(d))
            curr = curr.next
        
        return reverse_list(dummy.next)


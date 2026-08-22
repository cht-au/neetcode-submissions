# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None


        prev_n = None
        curr_n = head
        next_n = head.next
        while next_n:
            curr_n.next = prev_n
            prev_n = curr_n
            curr_n = next_n
            next_n = curr_n.next

        curr_n.next = prev_n

        # print(prev_n.val, curr_n.val, next_n)

        return curr_n
        

    # None <- 0 1 -> 2 -> 3
    #         p c    n
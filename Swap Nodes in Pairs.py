# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        origin_head=head
        while head:
            neibor=head.next
            if not neibor:
                break
            head.val,neibor.val=neibor.val,head.val
            head=neibor.next
        return origin_head
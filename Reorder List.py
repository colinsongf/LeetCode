# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return nothing
    def reverseList(self, head):
        if not head or not head.next:
            return head
        newhead=None
        prevnode,current=head,head.next
        prevnode.next=None
        while current:
            nextone=current.next
            current.next=prevnode
            prevnode=current
            if not nextone:
                newhead=current
            current=nextone
        return newhead

    def reorderList(self,head):
        if not head:
            return None
        newlist=None
        prevnode=head
        firstsp=head.next
        if not firstsp:
            return firstsp
        secondsp=firstsp.next
        if not secondsp:
            newlist=firstsp
            prevnode.next=None
        else:
            while secondsp and secondsp.next:
                prevnode=firstsp
                firstsp=firstsp.next
                secondsp=secondsp.next
                if not secondsp:
                    break
                secondsp=secondsp.next
            newlist=firstsp
            prevnode.next=None
        #merge
        firstsp,secondsp=head,self.reverseList(newlist)
        while firstsp and secondsp:
            origin_fnext,origin_snext=firstsp.next,secondsp.next
            firstsp.next=secondsp
            if origin_fnext:
                secondsp.next=origin_fnext
            secondsp=origin_snext
            firstsp=origin_fnext
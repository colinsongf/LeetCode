class ListNode(object):
    """docstring for ListNode"""
    def __init__(self, x):
        super(ListNode, self).__init__()
        self.val = x
        self.next=None
        
class Solution:
    def getMiddle(self, head):
        #at least 2 items in list will come in this function.
        firstsp = secondsp = head
        while secondsp.next and secondsp.next.next:
            secondsp=secondsp.next.next
            firstsp=firstsp.next
        return firstsp
    def mergeList(self, head1,head2):
        newhead=None
        sp1,sp2 = head1,head2
        if sp1.val < sp2.val:
            newhead=sp1
            sp1 = sp1.next
        else:
            newhead=sp2
            sp2 = sp2.next
        mergehead = newhead
        while sp1 and sp2:
            if sp1.val <sp2.val:
                mergehead.next = sp1
                sp1 = sp1.next
            else:
                mergehead.next = sp2
                sp2=sp2.next
            mergehead = mergehead.next
        while sp1:
            mergehead.next = sp1
            sp1 = sp1.next
            mergehead = mergehead.next
        while sp2:
            mergehead.next = sp2
            sp2 = sp2.next
            mergehead = mergehead.next
        return newhead

    def sortList(self, head):
        if not head or not head.next:
            return head
        mid = self.getMiddle(head)
        head1,head2 = head,mid.next
        mid.next = None
        head1 = self.sortList(head1)
        head2 = self.sortList(head2)
        head = self.mergeList(head1,head2)
        return head

class ListNode(object):
    """docstring for ListNode"""
    def __init__(self, x):
        super(ListNode, self).__init__()
        self.val = x
        self.next=None

class Solution:
    def removeElements(self, head, val):
        current=head
        prev=None
        newhead=None
        while current:
            if current.val==val:
                if prev:
                    prev.next=current.next
            else:
                prev=current
                if not newhead:
                    newhead=current
            current=current.next
        return newhead

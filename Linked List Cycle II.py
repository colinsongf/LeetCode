class ListNode(object):
    """docstring for ListNode"""
    def __init__(self, x):
        super(ListNode, self).__init__()
        self.val = x
        self.next=None
        
class Solution(object):
    def detectCycle(self, head):
        ret = None
        if not head:
            return ret
        firstsp,secondsp=head.next,head
        if not firstsp:
            return ret
        secondsp=secondsp.next
        if not secondsp:
            return ret
        secondsp=secondsp.next
        if not secondsp:
            return ret
        while firstsp and secondsp:
            if firstsp==secondsp:
                break
            firstsp=firstsp.next
            secondsp=secondsp.next
            if not secondsp:
                return ret
            secondsp=secondsp.next

        if not firstsp or not secondsp:
            return ret

        firstsp = head
        while firstsp and secondsp:
            if firstsp == secondsp:
                return firstsp
            firstsp,secondsp = firstsp.next,secondsp.next
        return ret

mylist0 = ListNode(3)
mylist1 = ListNode(2)
mylist2 = ListNode(0)
mylist3 = ListNode(-4)
mylist3.next=mylist0
mylist2.next=mylist3
mylist1.next=mylist2
mylist0.next=mylist1
ins=Solution()
ins.detectCycle(mylist0)

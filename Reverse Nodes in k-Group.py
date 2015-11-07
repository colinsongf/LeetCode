
class ListNode(object):
    """docstring for ListNode"""
    def __init__(self, x):
        super(ListNode, self).__init__()
        self.val=x
        self.next=None

def createList(array):
    if len(array)==1:
        return ListNode(array[0])
    head=ListNode(array[0])
    prev=head
    for i in array[1:]:
        current=ListNode(i)
        prev.next=current
        prev=current
    return head

def displayList(head):
    while head:
        print head.val,
        head=head.next
    print

class Solution:
    def reverseList(self,head,rear):
        prev=None
        newhead=newrear=None
        end=rear.next
        while head and head!=end:
            next=head.next
            head.next=prev
            if not prev:
                newrear=head
            prev=head
            head=next
        newhead=rear
        return (newhead,newrear)
    def getKsubrear(self,head,k):
        i=0
        while i<k-1 and head:
            head=head.next
            i+=1
        return head
    def reverseKGroup(self,head,k):
        headsp=head
        newlisthead=None
        rearsp=self.getKsubrear(head,k)
        if not rearsp:
            return head
        nextsub=rearsp.next
        newhead,newrear=self.reverseList(headsp,rearsp)

        newrear.next=None
        
        newlisthead=newhead
        prevsubrear=newrear
        headsp=nextsub
        
        while headsp:
            rearsp=self.getKsubrear(headsp,k)
            if rearsp:
                nextsub=rearsp.next
                newhead,newrear=self.reverseList(headsp,rearsp)
                prevsubrear.next=newhead
                newrear.next=None
                headsp=nextsub
                prevsubrear=newrear
            else:
                prevsubrear.next=headsp
                return newlisthead
        return newlisthead

ins=Solution()
head=createList([1,2,3,4,5])
head=ins.reverseKGroup(head,2)
displayList(head)

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

def createList(array):
	if not array:
		return None
	head=ListNode(array[0])
	prev=head
	for i in array[1:]:
		prev.next=ListNode(i)
		prev=prev.next
	return head

def displayList(head):
	while head:
		print head.val,
		head=head.next
	print

ins=Solution()

originlist=createList([1,2,6,3,4,5,6])
displayList(originlist)
newlist=ins.removeElements(originlist,6)
displayList(newlist)
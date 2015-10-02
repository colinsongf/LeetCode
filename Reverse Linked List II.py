class ListNode(object):
	"""docstring for ListNode"""
	def __init__(self, x):
		super(ListNode, self).__init__()
		self.val = x
		self.next=None
		
class Solution:
	def reverseBetween(self ,head ,m, n):
		firstsp = secondsp = None
		m-=1
		while m:
			if firstsp:
				firstsp = firstsp.next
			else:
				firstsp = head
			m-=1
		while n:
			if secondsp:
				secondsp = secondsp.next
			else:
				secondsp = head
			n-=1
		subhead = firstsp.next if firstsp else head
		subrear = secondsp
		nextrear = secondsp.next
		subrear.next = None
		current = subhead
		prevnode = None
		while current:
			nextone=current.next
			current.next=prevnode
			prevnode=current
			current=nextone
		if firstsp:
			firstsp.next=subrear
		else:
			head = subrear
		subhead.next = nextrear
		return head

def create_list(array):
	lists=ListNode(array[0])
	current=lists
	for item in array[1:]:
		current.next=ListNode(item)
		current=current.next
	return lists

def disp(lists):
	while lists:
		print lists.val,'->',
		lists=lists.next

if __name__ == '__main__':
	ins=Solution()
	mylist=create_list([1,2,3,4,5])
	disp(ins.reverseBetween(mylist,2,4))
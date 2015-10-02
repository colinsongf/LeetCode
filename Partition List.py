class ListNode(object):
	"""docstring for ListNode"""
	def __init__(self, x):
		super(ListNode, self).__init__()
		self.val = x
		self.next=None

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

class Solution:
	def partition(self, head, x):
		if not head:
			return head
		small_head,small_rear,big_head,big_rear = None,None,None,None
		while head:
			if head.val < x:
				if not small_head:
					small_head = head
				if small_rear:
					small_rear.next = head
				small_rear = head
				head=head.next
				small_rear.next=None
			else:
				if not big_head:
					big_head=head
				if big_rear:
					big_rear.next=head
				big_rear = head
				head=head.next
				big_rear.next=None
		if small_head:
			head=small_head
			small_rear.next=big_head
		else:
			head=big_head
		return head

mylist = create_list([1])

ins=Solution()

disp(ins.partition(mylist,0))
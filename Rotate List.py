class ListNode(object):
	"""docstring for ListNode"""
	def __init__(self, x):
		super(ListNode, self).__init__()
		self.val = x
		self.next=None
		
class Solution:
	#method 1
	"""
	def rotateRight(self,head,k):
		array = []
		current = head
		while current:
			array.append(current.val)
			current = current.next
		size=len(array)
		if not size:
			return head
		k=k%size
		array[:(0-k)]=reversed(array[:(0-k)])
		print array
		array[(0-k):]=reversed(array[(0-k):])
		print array
		array[:] = reversed(array[:])
		print array
		current = head
		i = 0
		while current:
			current.val = array[i]
			i+=1
			current=current.next
		return head
	"""
	def rotateRight(self, head, k):
		current = head
		rear = None
		size = 0
		while current:
			size += 1
			if not current.next:
				rear = current
			current = current.next
		if not size:
			return head
		k %= size
		if not k :
			return head
		firstsp,secondsp=head,head
		while k:
			secondsp=secondsp.next
			k -= 1
		while secondsp.next:
			firstsp = firstsp.next
			secondsp = secondsp.next
		newhead = firstsp.next
		firstsp.next = None
		secondsp.next = head
		return newhead

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
	mylist=create_list([1])
	disp(ins.rotateRight(mylist,2))
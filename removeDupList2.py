#!/usr/bin/python

class ListNode:
	def __init__(self,x):
		self.val=x
		self.next=None
		self.prev=None
class Solution:
	def deleteDuplicates(self,head):
		if not head:
			return head
		retlist=ListNode(-2**31)
		flag = False
		parent = retlist
		parent_of_parent = None
		while head:
			if head.val == parent.val:
				flag = True
			else:
				if flag:
					parent.val = head.val
					flag = False
				else:
					parent.next = ListNode(head.val)
					parent_of_parent = parent
					parent = parent.next
			head=head.next
		if flag:
			parent_of_parent.next=None
		return retlist.next

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
	mylist=create_list([1,2,2,3,3])
	disp(ins.deleteDuplicates(mylist)) 
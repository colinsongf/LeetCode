#!/usr/bin/python

class ListNode:
	def __init__(self,x):
		self.val=x
		self.next=None
class Solution:
	def deleteDuplicates(self,head):
		if not head:
			return head
		retlist,current=head,head
		preval = head.val
		neibor =head.next
		while neibor:
			if neibor.val != preval:
				current.next = neibor
				preval = neibor.val
				current = neibor
			neibor=neibor.next
			current.next = None
		return retlist

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
	mylist=create_list([1,1,2,3,3])
	disp(ins.deleteDuplicates(mylist)) 
#!/usr/bin/python

class ListNode:
	def __init__(self,x):
		self.val=x
		self.next=None
class Solution:
	def getListLength(self,head):
		length = 0
		while head:
			length += 1
			head = head.next
		return length
	def getIntersectionNode(self,headA,headB):
		sizeA,sizeB=self.getListLength(headA),self.getListLength(headB)
		answerNode = None
		i = 0
		if sizeA>sizeB:
			while i < sizeA-sizeB:
				i += 1
				headA=headA.next
		else:
			while i < sizeB-sizeA:
				i += 1
				headB = headB.next
		while headA and headB and not answerNode:
			if headA == headB:
				answerNode = headA
			headA,headB = headA.next,headB.next
		return answerNode

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
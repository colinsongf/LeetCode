#!/usr/bin/python

class ListNode:
	def __init__(self,x):
		self.val=x
		self.next=None
class Solution:
	def addTwoNumbers(self,list1,list2):
		ret=(list1.val+list2.val)/10
		val=(list1.val+list2.val)%10
		retList=ListNode(val)
		current=retList
		list1,list2=list1.next,list2.next
		while list1 and list2:
			val=(list1.val+list2.val+ret)%10
			ret=(list1.val+list2.val+ret)/10
			current.next=ListNode(val)
			current=current.next
			list1,list2=list1.next,list2.next
		solist=list1 if list1 else list2
		while solist:
			val=(solist.val+ret)%10
			ret=(solist.val+ret)/10
			current.next=ListNode(val)
			current=current.next
			solist=solist.next
		if ret:
			current.next=ListNode(ret)
		return retList
	def removeNthfromend(self,head,n):
		tmphead,firstsp,secondsp=head,head,None
		while n:
			secondsp=tmphead.next
			tmphead=tmphead.next
			n-=1
		if not secondsp:
			newhead=head.next
			del head
			return newhead
		while secondsp.next:
			firstsp,secondsp=firstsp.next,secondsp.next
		target=firstsp.next
		newnext=target.next
		del target
		firstsp.next=newnext
		return head
	def getminpos(self,lists):
		minpos,minvalue=-1,2**30
		for i,node in enumerate(lists):
			if node:
				if node.val < minvalue:
					minvalue = node.val
					minpos = i
		return minpos
	def mergeKList(self,lists):
		import heapq
		mergedList,current=None,None
		heap=[]
		heapsize=0
		for list in lists:
			heapq.heappush(heap,(list.val,list.next))
			heapsize+=1
		while heapsize:
			top = heapq.heappop(heap)
			heapsize-=1
			newnode=ListNode(top[0])
			if current:
				current.next=newnode
			else:
				mergedList=newnode
			if top[1]:
				heapq.heappush(heap,(top[1].val,top[1].next))
				heapsize+=1
			current=newnode
		return mergedList
	def mergeKLists(self,lists):
		size=len(lists)
		if size==0:
			return None
		if size==1:
			return lists[0]
		l_lists,r_lists=lists[:size/2],lists[size/2:]
		l_list,r_list=self.mergeKLists(l_lists),self.mergeKLists(r_lists)
		newlist,current=None,None
		while l_list and r_list:
			newnode=None
			if l_list.val<r_list.val:
				newnode=ListNode(l_list.val)
				l_list=l_list.next
			else:
				newnode=ListNode(r_list.val)
				r_list=r_list.next
			if not current:
				newlist=newnode
			else:
				current.next=newnode
			current=newnode
		while l_list:
			newnode=ListNode(l_list.val)
			if not current:
				newlist=newnode
			else:
				current.next=newnode
			current=newnode
			l_list=l_list.next
		while r_list:
			newnode=ListNode(r_list.val)
			if not current:
				newlist=newnode
			else:
				current.next=newnode
			current=newnode
			r_list=r_list.next
		return newlist

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
	list1=create_list([1,5,9,13])
	list2=create_list([3,19])
	list3=create_list([2,4,5,7,9,10])
	ins=Solution()
	#lists=[list1,list2,list3]
	list1=None
	lists=[list1]
	print ins.mergeKLists([None])
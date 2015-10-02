class ListNode(object):
	"""docstring for ListNode"""
	def __init__(self, x):
		self.val = x
		self.next=None

class Solution:
	def reverseList(self, head):
		if not head or not head.next:
			return head
		newhead=None
		prevnode,current=head,head.next
		prevnode.next=None
		while current:
			nextone=current.next
			current.next=prevnode
			prevnode=current
			if not nextone:
				newhead=current
			current=nextone
		return newhead

	def reorderList(self,head):
		if not head:
			return None
		newlist=None
		prevnode=head
		firstsp=head.next
		if not firstsp:
			return firstsp
		secondsp=firstsp.next
		if not secondsp:
			newlist=firstsp
			prevnode.next=None
		else:
			while secondsp and secondsp.next:
				prevnode=firstsp
				firstsp=firstsp.next
				secondsp=secondsp.next
				if not secondsp:
					break
				secondsp=secondsp.next
			newlist=firstsp
			prevnode.next=None
		#merge
		firstsp,secondsp=head,self.reverseList(newlist)
		while firstsp and secondsp:
			origin_fnext,origin_snext=firstsp.next,secondsp.next
			firstsp.next=secondsp
			if origin_fnext:
				secondsp.next=origin_fnext
			secondsp=origin_snext
			firstsp=origin_fnext

def looklist(node):
	if not node:
		return
	print node.val
	looklist(node.next)

node1=ListNode(1)
node2=ListNode(2)
node3=ListNode(3)
node4=ListNode(4)
node5=ListNode(5)
node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node5

ins=Solution()

ins.reorderList(None)
looklist(node1)
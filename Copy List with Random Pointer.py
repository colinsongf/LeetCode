class RandomListNode(object):
	"""docstring for Rand"""
	def __init__(self, x):
		self.label = x
		self.next = None
		self.random = None

class Solution:
	def copyRandomList(self,head):
		if not head:
			return None
		dicts={}#old_pointer=>new_pointer
		newhead=RandomListNode(head.label)
		dicts[head]=newhead

		queue=[head]
		while queue:
			top=queue.pop(0)
			if top.next:
				if top.next in dicts:
					dicts[top].next=dicts[top.next]
				else:
					dicts[top.next]=RandomListNode(top.next.label)
					dicts[top].next=dicts[top.next]
					queue.append(top.next)
			if top.random:
				if top.random in dicts:
					dicts[top].random=dicts[top.random]
				else:
					dicts[top.random]=RandomListNode(top.random.label)
					dicts[top].random=dicts[top.random]
					queue.append(top.random)
		return newhead

def looklist(node):
	if not node:
		return
	print node.label
	looklist(node.next)

ins=Solution()

node1=RandomListNode(1)
node2=RandomListNode(2)
node3=RandomListNode(3)
node4=RandomListNode(4)
node5=RandomListNode(5)
node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node5

newnode=ins.copyRandomList(node1)

looklist(newnode)
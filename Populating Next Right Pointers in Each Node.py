class TreeNode:
	def __init__(self,x):
		self.val=x
		self.left=self.right=self.next=None

class Solution:
	def connect_array(self,array):
		if not array:
			return
		prev=array[0]
		print len(array)
		for current in array[1:]:
			prev.next=current
			prev=current
	def connect(self,root):
		if not root:
			return
		queue1,queue2=[],[]
		queue1.append(root)
		while queue1:
			top=queue1.pop(0)
			if top.left:
				queue2.append(top.left)
			if top.right:
				queue2.append(top.right)
			if not queue1:
				self.connect_array(queue2)
				queue1=queue2
				queue2=[]


root=TreeNode(0)
root1=TreeNode(1)
root1.left=TreeNode(3)
root1.right=TreeNode(4)
root2=TreeNode(2)
root2.left=TreeNode(5)
root2.right=TreeNode(6)
root.left=root1
root.right=root2

ins=Solution()
ins.connect(root)
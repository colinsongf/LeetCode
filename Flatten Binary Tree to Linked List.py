class TreeNode(object):
	"""docstring for TreeNode"""
	def __init__(self, x):
		self.val=x
		self.left=self.right=None

class Solution:
	def arrage(self,root):
		rear=root
		origin_right=root.right
		if root.left:
			root.right,rear=self.arrage(root.left)
			root.left=None
		if origin_right:
			rear.right,rear=self.arrage(origin_right)
		return root,rear

	def flatten(self,root):
		if not root:
			return root
		self.arrage(root)

def looktree(root):
	if not root:
		return
	print root.val
	looktree(root.right)

tree1=TreeNode(1)
tree2=TreeNode(2)
tree3=TreeNode(3)
tree4=TreeNode(4)
tree5=TreeNode(5)
tree6=TreeNode(6)

tree1.left=tree2
tree1.right=tree5

tree2.left=tree3
tree2.right=tree4

tree5.right=tree6

ins=Solution()
ins.flatten(tree1)

looktree(tree1)
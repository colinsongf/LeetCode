class TreeNode(object):
	"""docstring for TreeNode"""
	def __init__(self, x):
		self.val=x
		self.left=self.right=None
		
class Solution:
	def __init__(self):
		self.infixOrder=[]
		self.sp=0
	def infix(self,root):
		if not root:
			return
		self.infix(root.left)
		self.infixOrder.append(root.val)
		self.infix(root.right)
	def infix_write(self,root):
		if not root:
			return
		self.infix_write(root.left)
		root.val=self.infixOrder[self.sp]
		self.sp+=1
		self.infix_write(root.right)
	def recoverTree(self,root):
		self.infix(root)
		self.infixOrder.sort()
		self.infix_write(root)
		return root
	def infix_debug(self,root):
		if not root:
			return
		self.infix_debug(root.left)
		print (root.val)
		self.infix_debug(root.right)

tree=TreeNode(5)
tree7=TreeNode(7)
tree1=TreeNode(1)
tree9=TreeNode(9)
tree.left=tree7
tree.right=tree9
tree7.left=tree1
tree7.right=TreeNode(4)
tree1.right=TreeNode(2)
tree9.left=TreeNode(3)
tree9.right=TreeNode(10)

ins=Solution()
ins.infix_debug(tree)
ins.recoverTree(tree)
print '==='
ins.infix_debug(tree)
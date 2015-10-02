class TreeNode:
	def __init__(self, x):
		self.x = x
		self.left = None
		self.right = None

class Solution:
	def getHeight(self,root):
		if not root:
			return 0
		if not root.left and not root.right:
			return 1
		elif not root.left:
			return self.getHeight(root.right)+1
		elif not root.right:
			return self.getHeight(root.left)+1
		hl,hr = self.getHeight(root.left),self.getHeight(root.right)
		return min(hl,hr)+1
	def minDepth(self, root):
		status = self.getHeight(root)
		return status
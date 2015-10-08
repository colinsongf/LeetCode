# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

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
		return max(hl,hr)+1
	def maxDepth(self, root):
		status = self.getHeight(root)
		return status
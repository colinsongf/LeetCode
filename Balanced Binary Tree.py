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
		hl,hr = self.getHeight(root.left),self.getHeight(root.right)
		if hl == -1 or hr == -1 or abs(hl-hr)>1:
			return -1
		else:
			return max(hr,hl)+1

	def isBalanced(self, root):
		status = self.getHeight(root)
		return (status>=0)
        
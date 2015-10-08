
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
	def isSameTree(self,root1,root2):
		if not root1 and not root2:
			return True
		elif not root1 or not root2:
			return False
		else:
			if root1.val != root2.val:
				return False
			left=self.isSameTree(root1.left,root2.left)
			right=self.isSameTree(root1.right,root2.right)
			return left and right
	def reverseTree(self,root):
		if not root:
			return None
		else:
			node=TreeNode(root.val)
			node.left=self.reverseTree(root.right)
			node.right=self.reverseTree(root.left)
			return node
	def isSymmetric(self,root):
		reversetree=self.reverseTree(root)
		return self.isSameTree(root,reversetree)
        
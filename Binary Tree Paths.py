# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	def __init__(self):
		self.answer = []
	def createAnswer(self, path):
		answer = '%d' % path[0]
		for i in path[1:]:
			answer += '->%d' % i
		return answer
	def findPath(self, path ,root):
		mypath = path[:]
		mypath.append(root.val)
		if not root.left and not root.right:
			subanswer = self.createAnswer(mypath)
			self.answer.append(subanswer)
			return
		if root.left:
			self.findPath(mypath, root.left)
		if root.right:
			self.findPath(mypath, root.right)
	def binaryTreePaths(self, root):
		if not root:
			return self.answer
		path = []
		self.findPath(path, root)
		return self.answer

from random import randint

class TreeNode(object):
	def __init__(self, vertex):
		self.vertex=vertex
		self.left=self.right=None
		self.parent=None

def insertTreeNode(currentRoot,node):
	if not currentRoot:
		return node
	if currentRoot.vertex > node.vertex:
		currentRoot.left=insertTreeNode(currentRoot.left,node)
		currentRoot.left.parent=currentRoot
	else:
		currentRoot.right=insertTreeNode(currentRoot.right,node)
		currentRoot.right.parent=currentRoot
	return currentRoot

def findleftmost(root):
	while root.left:
		root=root.left
	return root

def findNode(tree,vertex):
	current=tree
	while current and current.vertex!=vertex:
		if current.vertex > vertex:
			current=current.left
		else:
			current=current.right
	return current

def removeTreeNode(root,node):
	parentnode=node.parent
	newroot=root
	if node.left and node.right:
		righttree=node.right		
		right_leftmost=findleftmost(righttree)
		node.vertex=right_leftmost.vertex
		if right_leftmost.parent.left==right_leftmost:
			right_leftmost.parent.left=right_leftmost.right
			if right_leftmost.right:
				right_leftmost.right.parent=right_leftmost.parent
		else:
			right_leftmost.parent.right=right_leftmost.right
			if right_leftmost.right:
				right_leftmost.right.parent=right_leftmost.parent
		del right_leftmost
	elif node.left or node.right:
		if node.left:
			node.left.parent=parentnode
			if parentnode:
				if parentnode.left==node:
					parentnode.left=node.left
				else:
					parentnode.right=node.left
			else:
				newroot=node.left
		else:
			node.right.parent=parentnode
			if parentnode:
				if parentnode.left==node:
					parentnode.left=node.right
				else:
					parentnode.right=node.right
			else:
				newroot=node.right
		del node 
	else:
		if parentnode:
			if parentnode.left==node:
				parentnode.left=None
			else:
				parentnode.right=None
		else:
			newroot=None
		del node
	return newroot

def insertTreeNode_and_Check(currentRoot,node,t):
	current=currentRoot
	flag=False
	parent=None
	while current:
		parent=current
		if abs(current.vertex - node.vertex) <=t:
			flag=True
		if current.vertex <= node.vertex:
			current=current.right
		else:
			current=current.left
	if parent.vertex<=node.vertex:
		parent.right=node
	else:
		parent.left=node
	node.parent=parent
	return flag

def infix(root):
	if root:
		infix(root.left)
		print root.vertex,
		infix(root.right)

class Solution:
	def containsNearbyAlmostDuplicate(self, nums, k, t):
		size=len(nums)
		if not size or not k:
			return False
		if k>size-1:
			k=size-1
		tree=TreeNode(nums[0])

		for i in range(1,k+1):
			node=TreeNode(nums[i])
			flag=insertTreeNode_and_Check(tree,node,t)
			if flag:
				return True
		todelete=0
		for i in range(k+1,size):
			#delete todelete
			node=findNode(tree,nums[todelete])
			todelete+=1
			tree=removeTreeNode(tree,node)
			newnode=TreeNode(nums[i])
			if tree:
				if insertTreeNode_and_Check(tree,newnode,t):
					return True
			else:
				tree=newnode
		return False

class TreeNode:
	def __init__(self, x):
		self.val=x
		self.left=self.right=None

class Solution:
	def zigzagLevelOrder(self, root):
		if not root:
		    return []
		cur,size = 0,1
		queue,retList,currentList=[],[],[]
		queue.append(root)
		while cur<size:
			end = len(queue)
			while cur<end:
				top=queue[cur]
				currentList.append(top.val)
				if top.right:
					queue.append(top.right)
					size += 1
				if top.left:
					queue.append(top.left)
					size += 1
				cur+=1
			if len(retList)%2==0:
				currentList.reverse()
			retList.append(currentList)
			currentList=[]
		return retList

ins=Solution()

node1=TreeNode(1)
node2=TreeNode(2)
node3=TreeNode(3)
node4=TreeNode(4)
node5=TreeNode(5)
node1.left=node2
node1.right=node3
node2.left=node4
node2.right=node5

print ins.zigzagLevelOrder(node1)
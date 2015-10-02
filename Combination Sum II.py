class Answer(object):
	"""docstring for ClassName"""
	def __init__(self, vertex ,parent, summary ,i):
		self.parent=parent
		self.vertex=vertex
		self.summary=summary
		self.i=i

def getPath(ansroot):
	path=[]
	while ansroot.vertex!=-1:
		path.append(ansroot.vertex)
		ansroot=ansroot.parent
	return path[::-1]

class Solution:
	def combinationSum2(self, candidates,target):
		root=Answer(-1,None,0,-1)
		stack=[]
		stack.append(root)
		candidates.sort()
		answerList=[]
		while stack:
			top=stack.pop()
			if top.summary>target:
				continue
			elif top.summary==target:
				ianswer=getPath(top)
				if ianswer not in answerList:
					answerList.append(ianswer)
				continue
			for i,candidate in enumerate(candidates):
				if top.i>=i or candidate < top.vertex:
					continue
				if top.summary+candidate>target:
					break
				nextroot=Answer(candidate,top,top.summary+candidate,i)
				stack.append(nextroot)
		return answerList

ins=Solution()
print ins.combinationSum2([10,1,2,7,6,1,5],8)
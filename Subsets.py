class Solution(object):
	def getAnswer(self,answer,array):
		finalAns=[]
		for ans,rans in zip(answer,array):
			if ans:
				finalAns.append(rans)
		return finalAns
	def subsets(self,array):
		answerList = []
		array.sort()
		n = len(array)
		answer,record = [0 for x in range(n)],[0 for x in range(n)]
		step=0
		record[step]=-1
		while step>=0:
			record[step]+=1
			if record[step]==2:
				step-=1
			else:
				answer[step]=record[step]
				if step==n-1:
					answerList.append(self.getAnswer(answer,array))
				else:
					step+=1
					record[step]=-1
		return answerList

ins=Solution()
print ins.subsets([1,2,3])
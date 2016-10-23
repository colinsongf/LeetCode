class Solution(object):
	def getAnswer(self,answer):
		finalAns=[]
		for i,ans in enumerate(answer):
			if ans:
				finalAns.append(i+1)
		return finalAns
	def combine(self,n,k):
		answerList = []
		answer,record = [0 for x in range(n)],[0 for x in range(n)]
		step=0
		record[step]=-1
		while step>=0:
			summary = sum(answer[:step])
			record[step]+=1
			while record[step]<2 and summary>k:
				record[step]+=1
			if record[step]==2:
				step-=1
			else:
				answer[step]=record[step]
				if step==n-1 and summary+record[step]==k:
					answerList.append(self.getAnswer(answer))
				elif step<n-1:
					step+=1
					record[step]=-1
		return answerList

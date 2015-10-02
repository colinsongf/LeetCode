class Solution(object):
	def getSubSummary(self,answer,step,num_type):
		summary = 0
		for i,ans in enumerate(answer[:step]):
			summary+=ans*num_type[i]
		return summary
	def getAnswer(self,answer,num_type):
		this_answer = []
		for ans,num in zip(answer,num_type):
			while ans:
				this_answer.append(num)
				ans-=1
		return this_answer
	def subsetsWithDup(self, array):
		hashmap={}
		for num in array:
			hashmap[num]=1 if num not in hashmap else hashmap[num]+1
		num_type=sorted(hashmap.keys())
		size = len(num_type)
		answerList = []
		answer,record = [0 for x in range(size)],[0 for x in range(size)]
		step=0
		record[step]=-1
		while step>=0:
			record[step]+=1
			summary = self.getSubSummary(answer,step,num_type)
			if record[step]>hashmap[num_type[step]]:
				step-=1
			elif step == size-1:
				answer[step]=record[step]
				this_answer=self.getAnswer(answer,num_type)
				answerList.append(this_answer)
			else:
				answer[step]=record[step]
				step+=1
				record[step]=-1
		return answerList

ins=Solution()
print ins.subsetsWithDup([1,2,2])
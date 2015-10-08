class Solution:
    # @param {integer} k
    # @param {integer} n
    # @return {integer[][]}
	def __init__(self):
		self.answers=[]
	def backtrace(self, step, answer ,k , n):
		if step==k:
			if sum(answer)==n:
				self.answers.append(answer[:])
			return 
		subsummary=sum(answer[:step])
		if step==0:
			for i in range(1,10):
				if i not in answer[:step] and subsummary+i<=n:
					answer[step]=i
					self.backtrace(step+1,answer,k,n)
		else:
			for i in range(answer[step-1],10):
				if i not in answer[:step] and subsummary+i<=n:
					answer[step]=i
					self.backtrace(step+1,answer,k,n)

	def combinationSum3(self, k, n):
		answer=[0]*k
		self.backtrace(0,answer,k,n)
		return self.answers
class Solution:
	def getanswer(self,m,i,j,candidates):
		answer=[]
		while i>=0 and j>0:
			k=m[i][j]
			j-=k*candidates[i]
			while k:
				answer.append(candidates[i])
				k-=1
			i-=1
		answer.sort()
		return answer

	def combinationSum(self,candidates,target):
		size=len(candidates)
		m=[[0 for x in range(target+1)] for y in range(size)]
		answerlist=[]
		#init
		for i in range(size):
			m[i][0]=0
		for j in range(target+1):
			if j%candidates[0]==0:
				m[0][j]=j/candidates[0]
			else:
				m[0][j]=0
			if j==target:
				myanswer=self.getanswer(m,i,j,candidates)
				if myanswer:
					answerlist.append(myanswer)
		m[0][0]=1
		#dynamic
		for i in range(1,size):
			for j in range(1,target+1):
				for k in range(j/candidates[i]+1):
					if m[i-1][j-k*candidates[i]]:
						m[i][j]=k
						if j==target and k:
							myanswer=self.getanswer(m,i,j,candidates)
							if myanswer:
								answerlist.append(myanswer)
		print m
		return answerlist

ins=Solution()
print ins.combinationSum([2,3,5],7)
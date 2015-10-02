class Solution:
	def twoSum(self,answer,num,end,target):
		i,j=0,end
		while i<j:
			if num[i]+num[j]==target:
				previ,prevj=num[i],num[j]
				while i<end and num[i]==previ:
					i+=1
				while j>=0 and num[j]==prevj:
					j-=1
				thisanswer=[previ,prevj,-target]
				answer.append(thisanswer)
			elif num[i]+num[j]<target:
				i+=1
			else:
				j-=1
	def threeSum(self, num):
		answer=[]
		prev=None
		num.sort()
		size=len(num)
		if size<3:
			return answer
		for i in range(size-1,1,-1):
			if prev!=None and prev==num[i]:
				continue
			self.twoSum(answer,num,i-1,-num[i])
			prev=num[i]
		return answer

ins=Solution()
print ins.threeSum([0,0,0,0])
#"""[-1,0,1,2,-1,-4]"""
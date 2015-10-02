class Solution:
	def twoSum(self,num,answer,target,start,end,item1,item2):
		i,j=start,end
		flag=False
		while i<j:
			if num[i]+num[j]==target:
				previ,prevj=num[i],num[j]
				while i<=end and num[i]==previ:
					i+=1
				while j>=0 and num[j]==prevj:
					j-=1
				thisanswer=[item1,item2,previ,prevj]
				answer.append(thisanswer)
				flag=True
			elif num[i]+num[j]>target:
				j-=1
			else:
				i+=1
		return flag
	def fourSum(self, num, target):
		answer=[]
		size=len(num)
		num.sort()
		prev=None
		if size<4:
			return answer
		ever=[]
		for i in range(size-3):
			for j in range(i+1,size-2):
				if (num[i],num[j]) in ever:
					continue
				subtarget=target-(num[i]+num[j])
				if self.twoSum(num,answer,subtarget,j+1,size-1,num[i],num[j]):
					ever.append((num[i],num[j]))
				prev=num[j]
		return answer

ins=Solution()
print ins.fourSum([-492,-479,-468,-447,-432,-428,-418,-406,-388,-369,-300,-275,-238,-231,-228,-225,-224,-221,-220,-219,-189,-186,-180,-144,-130,-73,-67,-66,-55,-54,-53,-19,-6,13,28,36,47,57,80,82,87,97,97,120,132,142,148,174,176,176,205,225,232,238,245,247,264,268,268,275,319,334,387,392,412,413,426,434,442,451,475,478,485,490], 4631)
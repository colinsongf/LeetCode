class Solution:
    # @return an integer
	def __init__(self):
		self.min=self.answer=None
	def twoSum(self,num,end,target,numi):
		i,j=0,end
		while i<j:
			value=num[i]+num[j]
			if value==target:
				previ,prevj=num[i],num[j]
				while i<end and num[i]==previ:
					i+=1
				while j>=0 and num[j]==prevj:
					j-=1
				self.min=0
			elif value<target:
				if abs(value-target)<self.min:
					self.min=abs(value-target)
					self.answer=value+numi
				i+=1
			else:
				if abs(value-target)<self.min:
					self.min=abs(value-target)
					self.answer=value+numi
				j-=1
	def threeSumClosest(self, num, target):
		self.min=2**31
		prev=None
		num.sort()
		size=len(num)
		if size<3:
			return 0
		for i in range(size-1,1,-1):
			if prev!=None and prev==num[i]:
				continue
			self.twoSum(num,i-1,target-num[i],num[i])
			prev=num[i]
		return self.answer if self.min!=0 else target
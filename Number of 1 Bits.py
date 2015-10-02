class Solution:
	def hammingWeight(self,n):
		counter=0
		while n:
			n&=(n-1)
			counter+=1
		return counter

ins=Solution()
print ins.hammingWeight(11)
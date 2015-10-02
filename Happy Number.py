class Solution:
	def getBitResult(self, n):
		answer=0
		while n:
			answer+=(n%10)**2
			n/=10
		return answer
	def isHappy(self, n):
		n=self.getBitResult(n)
		if n==1:
			return True
		time=0
		while n>=10:
			n=self.getBitResult(n)
		return n==1

ins=Solution()
print ins.isHappy(19)
class Solution:
	def plusOne(self,digits):
		size=len(digits)
		nextbit = (digits[-1]+1)/10
		digits[-1] = (digits[-1]+1)%10
		for i in range(size-2,-1,-1):
			sub = digits[i]+nextbit
			digits[i] = sub%10
			nextbit =  sub/10
		if nextbit:
			digits[0:1]=[nextbit,digits[0]]
		return digits

ins = Solution()
print ins.plusOne([0])
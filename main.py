#!/usr/bin/python

class Solution:
	def isPalindrome(self,x):
		if x<10:
			return 1
		bit,number=0,x
		while number:
			bit+=1
			number/=10
		times,ten=0,10**(bit-1)
		ret=True
		ltmp,rtmp=x,x
		while times<bit/2 and ret:
			times+=1
			l,r=ltmp/ten,rtmp%10
			ltmp%=ten
			rtmp/=10
			ten/=10
			if l!=r:
				ret=False
		return 1 if ret else -1

a=Solution()
print a.isPalindrome(123321)

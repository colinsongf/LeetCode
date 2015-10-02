class Solution:
	def countPrimes(self,n):
		if n<=1:
			return 0
		array=[1 for x in range(n)]
		array[0]=array[1]=0
		for i in range(2,n):
			if not array[i]:
				continue
			for j in range(2,n/i+1):
				if j*i<n:
					array[i*j]=0
		counter=0
		for i in array:
			if i:
				counter+=1
		return counter

ins=Solution()

print ins.countPrimes(1500000)
class Solution:
	def maxProfit(self, prices):
		size=len(prices)
		m=[[0 for y in range(size)] for x in range(size)]
		for l in range(2,size):
			for i in range(size-l+1):
				j=i+l-1
				for k in range(i,j):
					m[i][j]=max(m[i][j],m[i][k]+m[k+1][j])
		return m[0][size]

ins=Solution()
print ins.maxProfit([1,2,4,2,5,7,2,4,9,0])
class Solution:
	def numTrees_method0(self, n):#xiaolv tai di
		if not n:
			return 1
		summary=0
		for i in range(n):
			left,right=i,n-i-1
			leftsum,rightsum=self.numTrees_method0(left),self.numTrees_method0(right)
			summary+=leftsum*rightsum
		return summary
	def numTrees_method1(self, n):
		func=[1,1,2]
		if n<=2:
			return func[n]
		i=3
		while i<=n:
			summary=0
			for j in range(i):
				summary+=func[j]*func[i-j-1]
			func.append(summary)
			i+=1
		return func[n]

ins=Solution()
print ins.numTrees_method1(4)
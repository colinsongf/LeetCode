class Solution:
	def getI(self, num,size):
		i,j=size-2,size-1
		while i>=0 and num[i]>=num[j]:
			i-=1;j-=1
		return i
	def permute(self,num):
		size=len(num)
		retAns=[]
		retAns.append(sorted(num))
		while True:
			currentNum=retAns[-1][:]
			i = self.getI(currentNum,size)
			if i<0:
				break
			currentNum[i+1:]=reversed(currentNum[i+1:])
			for j in range(i+1,size):
				if currentNum[j] > currentNum[i]:
					currentNum[i],currentNum[j]=currentNum[j],currentNum[i]
					break
			retAns.append(currentNum)
		return retAns

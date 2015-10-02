class Solution:
	def firstMissingPositive(self, array):
		size=len(array)
		for i in range(size):
			while array[i]>0 and array[i]-1<size and array[i]!=i+1 and array[array[i]-1]!=array[i]:
				pos1,pos2=i,array[i]-1
				array[pos1]^=array[pos2]
				array[pos2]^=array[pos1]
				array[pos1]^=array[pos2]
		for i in range(size):
			if array[i]!=i+1:
				return i+1
		return size+1

ins=Solution()
print ins.firstMissingPositive([2,1])#[3,4,-1,1])
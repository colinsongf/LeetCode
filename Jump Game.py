class Solution:
	def canJump(self, array):
		size=len(array)
		if size<2:
			return True
		step=array[0]
		for i in range(1,size-1):
			step-=1
			if step<0:
				return False
			step=max(step,array[i])
		return step>0

ins=Solution()

print ins.canJump([0,1])#false
print ins.canJump([0])#true
print ins.canJump([1,2,3])#true
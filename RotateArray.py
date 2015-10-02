class Solution:
	def rotate(self,nums,k):
		size=len(nums)
		if k>size:
			k%=size
		nums[(-1)*k:]=reversed(nums[(-1)*k:])
		nums[:(-1)*k]=reversed(nums[:(-1)*k])
		nums.reverse()
		return nums

ins=Solution()
print ins.rotate([1,2],3)
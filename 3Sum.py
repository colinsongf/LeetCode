class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def threeSum(self, nums):
		size=len(nums)
		ret=[]
		if size<3:
			return ret
		nums.sort()
		prevsel=nums[0]-1
		for i in range(size-2):
			current=nums[i]
			if prevsel==current:
				continue
			head,rear=i+1,size-1
			while head<rear:
				prevh,prevr=nums[head],nums[rear]
				if nums[head]+nums[rear]== -current:
					#print current,nums[head],nums[rear]
					ret.append([current,nums[head],nums[rear]])
					while head<size and nums[head]==prevh:
						head+=1
					while rear>=0 and nums[rear]==prevr:
						rear-=1
				elif nums[head]+nums[rear]> -current:
					while rear>=0 and nums[rear]==prevr:
						rear-=1
				else:
					while head<size and nums[head]==prevh:
						head+=1
			prevsel=current
		return ret
class Solution(object):
	def findPeakElement(self ,num):
		left,right=0,len(num)-1
		while left<=right:
			if left==right:
				return left
			mid=(left+right)/2
			if num[mid]<num[mid+1]:
				left=mid+1
			else:
				right=mid

ins=Solution()
print ins.findPeakElement([1,2,3])
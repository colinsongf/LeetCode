class Solution:
	def findMin(self,num):
		size=len(num)
		head,rear=0,size-1
		if size<2 or num[head]<num[rear]:
			return num[head]
		while head<rear:
			if head==rear-1:
				return num[rear]
			mid=head+rear>>1
			if num[mid]>num[head]:
				head=mid
			elif num[mid]<num[rear]:
				rear=mid
ins=Solution()
print ins.findMin([3,5,1,2])
class Solution:
	def trap(self, array):
		size=len(array)
		capacity=0
		if size<3:
			return capacity
		leftMaxHeight=array[0]
		leftheight=[-1 for x in range(size)]
		for i in range(1,size):
			if array[i]<leftMaxHeight:
				leftheight[i]=leftMaxHeight
			else:
				leftMaxHeight=array[i]
		rightMaxHeight=array[size-1]
		rightheight=[-1 for x in range(size)]
		for i in range(size-2,-1,-1):
			if array[i]<rightMaxHeight:
				rightheight[i]=rightMaxHeight
			else:
				rightMaxHeight=array[i]
		#print leftheight
		#print rightheight
		for i in range(1,size-1):
			if leftheight[i]!=-1 and rightheight[i]!=-1:
				capacity+=min(leftheight[i],rightheight[i])-array[i]
		return capacity
class Solution:
    # @param {integer} s
    # @param {integer[]} nums
    # @return {integer}
	def minSubArrayLen(self,target,array):
		size=len(array)
		if not size:
			return 0
		head,rear=0,0
		subsum=array[0]
		while subsum<target and rear<size:
			rear+=1
			if rear==size:
				return 0
			subsum+=array[rear]
		answer=rear-head+1
		while rear<size:
			while subsum-array[head] >=target:
				subsum-=array[head]
				head+=1
			answer=min(answer,rear-head+1)
			rear+=1
			if rear<size:
				subsum+=array[rear]
		return answer
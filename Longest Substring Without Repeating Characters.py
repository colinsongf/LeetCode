class Solution:
	def lengthOfLongestSubstring(self,string):
		if not string:
			return 0
		size=len(string)
		container=set()
		head=rear=0
		maxlength=1
		while rear<size:
			ch=string[rear]
			if ch in container:
				while string[head]!=ch:
					container.remove(string[head])
					head+=1
				head+=1
			else:
				container.add(ch)
			maxlength=max(maxlength,rear-head+1)
			rear+=1
		return maxlength

ins=Solution()
print ins.lengthOfLongestSubstring('tmmzuxt')
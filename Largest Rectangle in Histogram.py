class Solution:
	def largestRectangleArea(self, height):
		size=len(height)
		if not size:
			return 0
		if size==1:
			return height[0]
		maxarea=0
		stack=[]
		for i,hei in enumerate(height):
			if not stack or hei >= stack[-1][1]:
				stack.append((i,hei))
			else:
				last=-1
				while stack and stack[-1][1]>=hei:
					maxarea=max(maxarea,(i-stack[-1][0])*stack[-1][1])
					last=stack[-1][0]
					stack.pop()
				stack.append((last,hei))
		if stack:
			while stack:
				maxarea=max(maxarea,(size-stack[-1][0])*stack[-1][1])
				stack.pop()
		return maxarea

ins=Solution()
print ins.largestRectangleArea([2,1,2])
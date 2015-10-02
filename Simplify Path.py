class Solution:
	def simplifyPath(self, path):
		dirs=[x for x in path.split('/') if x]
		stack=[]
		for d in dirs:
			if d=='.':
				continue
			elif d=='..':
				if stack:
					stack.pop()
			else:
				stack.append(d)
		ret='/'
		for d in stack:
			ret+=d+'/'
		if len(ret)!=1 and ret[-1]=='/':
			ret=ret[:-1]
		return ret

ins=Solution()

print ins.simplifyPath('/home//foo/')
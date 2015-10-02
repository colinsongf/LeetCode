def isValid(s):
	stack=[]
	status = True
	hashmap={'(':')','{':'}','[':']'}
	for ch in s:
		if ch in hashmap.keys():
			stack.append(ch)
		elif ch in hashmap.values():
			if not stack:
				status=False
				break
			top=stack.pop()
			if hashmap[top]!=ch:
				status=False
				break
	return status
import sys
s=sys.argv[1]
print isValid(s)

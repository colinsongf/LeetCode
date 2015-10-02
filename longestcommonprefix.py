#!/usr/bin/python

class Solution:
	def longestCommonPrefix(self,strs):
		prefix=strs[0][:]
		for str in strs[1:]:
			pos,i=-1,0
			prefixsize=len(prefix)
			for ch in str:
				if i>=prefixsize:
					break
				if ch!=prefix[i]:
					pos=i
					break
				i+=1
			if pos!=-1:
				prefix=prefix[:pos]
			elif i<prefixsize:
				prefix=prefix[:i]
		return prefix

ins=Solution()
strs=['good','go']
print ins.longestCommonPrefix(strs)

def strStr(haystack,needle):
	stringsize,patternsize=len(haystack),len(needle)
	position,i=-1,0
	if stringsize<patternsize:
		return position;
	while i <= stringsize-patternsize:
		if haystack[i:i+patternsize]==needle:
			position=i
			break
		else:
			if i+patternsize>=stringsize:
				break
			ch=haystack[i+patternsize]
			inwhere=-1
			for j in range(patternsize-1,-1,-1):
				if needle[j]==ch:
					inwhere=j
					break
			i+=patternsize-inwhere
	return position

print strStr('iamleechanxdorc','leech')

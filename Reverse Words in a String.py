class Solution(object):
	def reverseWords(self, string):
		diction = []
		word = ''
		for ch in string:
			if ch==' ':
				if word:
					diction.append(word)
					word = ''
			else:
				word += ch
		if word:
			diction.append(word)
		diction.reverse()
		return ' '.join(diction)

ins = Solution()
print ins.reverseWords('   the sky    is blue ')
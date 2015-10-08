class Solution:
    # @param s, a string
    # @return an integer
	def lengthOfLastWord(self, string):
		length = 0
		string=string.strip()
		for s in string:
			if s==' ':
				length = 0
			else:
				length += 1
		return length
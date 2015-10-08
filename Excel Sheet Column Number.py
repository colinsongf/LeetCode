class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
		ret=0
		for ch in s:
			ret*=26
			ret+=(ord(ch)-ord('A')+1)
		return ret
class Solution:
    # @return a string
    def convertToTitle(self, num):
		bits,retStr='ZABCDEFGHIJKLMNOPQRSTUVWXY',''
		while num:
			retStr = bits[num%26]+retStr
			num= num/26 if num%26 else num/26-1
		return retStr
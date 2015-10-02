class Solution:
	def convertToTitle(self,num):
		bits='ZABCDEFGHIJKLMNOPQRSTUVWXY'
		retStr=''
		while num:
			retStr = bits[num%26]+retStr
			num= num/26 if num%26 else num/26-1
		return retStr

ins=Solution()
print ins.convertToTitle(28)
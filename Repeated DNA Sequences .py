class Solution:
	def changeToNum(self ,string):
		ret = 0
		bitmap={'G':0,'A':1,'T':2,'C':3}
		for i in range(10):
			ret*=10
			ret+=bitmap[string[i]]
		return ret
	def findRepeatedDnaSequences(self, s):
		retdict=[]
		size = len(s)
		if size<=10:
			return retdict
		record={}
		for i in range(9,size):
			substring=s[i-9:i+1]
			number=self.changeToNum(substring)
			if number in record:
				if substring not in retdict:
					retdict.append(substring)
			else:
				record[number]=1
		return retdict

ins=Solution()
print ins.findRepeatedDnaSequences("AAAAAAAAAAAA")